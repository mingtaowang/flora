import os
import shutil

from settings import CONFIG
from flora.utils.decorator import catch_func_exception


@catch_func_exception
def delete_suspects():
    # 每天固定时间删除
    if os.path.exists(CONFIG.base_path):
        shutil.rmtree(CONFIG.base_path)


# if __name__ == '__main__':
#     delete_suspects()
