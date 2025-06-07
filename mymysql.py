 
import pymysql
conn = pymysql.connect(host="127.0.0.1",port=3306,user="root",passwd="111728",charset="utf8",db="unicom")
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)#相当于去数据库去数据的手


cursor.execute("insert into admin(username,password,mobile) values('xl1','111728','17640628414')")

sql = " insert into admin(username,password,mobile) values(%s,%s,%s)"#防注入的动态添加
cursor.execute(sql,['xl2','111728','17640628414'])

sql = " insert into admin(username,password,mobile) values(%(name1)s,%(name2)s,%(name3)s)"#防注入的动态添加
cursor.execute(sql, {'name1':'xl3','name2' :'111728','name3': '17640628414'})
conn.commit()


cursor.execute("select * from admin where id>26 and username=%s ",['xl3'])
data = cursor.fetchall()
print(data)

cursor.execute("select * from admin where id>25 " )
data = cursor.fetchone()#获取第一个
print(data)

def dispaly(data):
    for i in data:
        print(i)


cursor.execute("delete from admin where id>24 ")
conn.commit()
cursor.execute("update admin set password = 666 where username='xl2' ")
conn.commit()
cursor.execute("select * from admin ")
data = cursor.fetchall()
dispaly(data)



cursor.close()
conn.close()













