# berry

## berry
| field | type| is null | desc |
|-----|-----|-----|------------|
| id | 	Number | NULLABLE | id |
| name | 	String | NULLABLE | get berry image url based on it |
| status | 	String | NULLABLE | audit status |

## audit
| field | type| is null | desc |
|-----|-----|-----|------------|
| berry_id | 	Number | NULLABLE | berry_id |
| note | 	STRING | NULLABLE | Custom note for the selected area |
| defect | 	STRING | NULLABLE | defect name selected by the auditor |
| x | 	Float | NULLABLE | x |
| y | 	Float | NULLABLE | y |
| weight | 	Float | NULLABLE | weight |
| height | 	Float | NULLABLE | height |