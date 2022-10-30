import insertUtil as ut
import psycopg2

# Đây là chương trình thực hiện kết nối và insert data vào PostgreSQl
conn = psycopg2.connect(database='covid_postgres', user='postgres', password='87654321', host='database-postgres.cd9eub73ylze.us-east-1.rds.amazonaws.com', port='5432')
print('Open DB successfully')
ut.insert(conn)
ut.select(conn)
conn.close()
print('Successfully')