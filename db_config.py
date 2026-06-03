import mysql.connector


def get_database_connection():

    connection = mysql.connector.connect(
        host='gateway01.ap-southeast-1.prod.aws.tidbcloud.com',
        user='2dFx9v9updQcJNc.root',
        password='tyRMXSYBUgu4jvaF',
        database='student_task_manager01',
        port= 4000
    )

    return connection