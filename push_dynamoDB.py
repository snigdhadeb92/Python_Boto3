import boto3
db = boto3.resource('dynamodb')
table = db.Table('employees')

table.put_item(
    Item={
        'emp_id':'2',
        'designation': 'Software Developer',
        'name': 'Amrita Mondal',
        'age':'26'
    }
)