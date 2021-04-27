# -*- coding: utf-8 -*-

import os
import sys
import time
import threading

import schedule
import winerror
import win32event
import win32service
import servicemanager
import win32serviceutil

from flora.app import create_app
from settings import CONFIG
from flora.service.task import delete_suspects

_ONE_DAY_IN_SECONDS = 30
app = create_app()


def thread_target():
    app.run(host=CONFIG.http_host, port=CONFIG.http_port, debug=CONFIG.debug, use_reloader=False)


def schedule_target():
    schedule.every().day.at(CONFIG.run_time).do(delete_suspects)
    while True:
        schedule.run_pending()
        time.sleep(_ONE_DAY_IN_SECONDS)


class FloraServiceClient(win32serviceutil.ServiceFramework):
    _svc_name_ = 'FloraServiceClient'
    _svc_display_name_ = 'Flora Tip Client'
    _svc_description_ = 'Flora tip client'

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        self.run = True

    def SvcDoRun(self):
        th = threading.Thread(target=thread_target)
        th.start()

        t = threading.Thread(target=schedule_target)
        t.start()
        try:
            while self.run:
                time.sleep(_ONE_DAY_IN_SECONDS)

        except KeyboardInterrupt:
            pass

        pass

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
        self.run = False


if __name__ == '__main__':
    if len(sys.argv) == 1:
        try:
            evtsrc_dll = os.path.abspath(servicemanager.__file__)
            servicemanager.PrepareToHostSingle(FloraServiceClient)
            servicemanager.Initialize('FloraServiceClient', evtsrc_dll)
            servicemanager.StartServiceCtrlDispatcher()
        except win32service.error as details:
            if details == winerror.ERROR_FAILED_SERVICE_CONTROLLER_CONNECT:
                win32serviceutil.usage()
    else:
        win32serviceutil.HandleCommandLine(FloraServiceClient)
