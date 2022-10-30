import insertUtil as ut
import MySQLdb

# Còn đây là chương trình thực hiện kết nối và insert data cho Aurora
conn = MySQLdb.connect(host='database-aurora.cluster-cd9eub73ylze.us-east-1.rds.amazonaws.com', user='admin', passwd='12345678', db='covid_aurora', port=3306)
print('Open DB successfully')
ut.insert(conn)
ut.select(conn)
conn.close()
print('Successfully')


