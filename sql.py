import pymysql
db=pymysql.connect(host="10.5.110.241",user="root",password="ts123456",db="codb")
cursor=db.cursor()
#时薪
sql='''SELECT u.user_id,u.uname,g.`name`
FROM ts_user u
INNER JOIN ts_group g
ON u.uid=g.uid
'''

cursor.execute(sql)

result=cursor.fetchall()
for x in result:
    print(x)

