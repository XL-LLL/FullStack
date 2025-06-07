from flask import Flask, render_template,request
import pymysql




app = Flask(__name__)



def select():
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="111728", charset="utf8", db="unicom")
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    cursor.execute("select * from admin ")
    data = cursor.fetchall()

    cursor.close()
    conn.close()
    return data

def insert(data):

    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="111728", charset="utf8", db="unicom")
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    sql = " insert into admin(username,password,mobile) values(%(name1)s,%(name2)s,%(name3)s)"
    cursor.execute(sql, {'name1': data['xinusername'], 'name2': data['xinpassword'], 'name3': data['xinmobile']})
    conn.commit()

    cursor.close()
    conn.close()

def updata(data):
    print(not data['gaiusername']=='',not data['gaipassword']=='',not data['gaimobile']=='')
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="111728", charset="utf8", db="unicom")
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    id = data['gaiid']
    if not data['gaiusername']=='':
        sql = "update admin set username = %(gaiusername)s where id=%(gaiid)s"
        cursor.execute(sql, {'gaiusername': data['gaiusername'],'gaiid': data['gaiid'] })
        conn.commit()
    if not data['gaipassword']=='':
        sql = "update admin set password = %(gaipassword)s where id=%(gaiid)s"
        cursor.execute(sql, {'gaipassword': data['gaipassword'],'gaiid': data['gaiid'] })
        conn.commit()
    if not data['gaimobile']=='':
        sql = "update admin set mobile = %(gaimobile)s where id=%(gaiid)s"
        cursor.execute(sql, {'gaimobile': data['gaimobile'],'gaiid': data['gaiid'] })
        conn.commit()
    cursor.close()
    conn.close()

def delete(data):
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="111728", charset="utf8", db="unicom")
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    sql = " delete from admin where id =%(shanid)s"
    cursor.execute(sql, {'shanid': data['shanid']})
    conn.commit()

    cursor.close()
    conn.close()


@app.route('/',methods=['POST','GET'])
def index():
    if request.method == 'GET':
        list = select()
        return render_template("mysql_wb.html",title = "数据库",data = list)

    data = request.form.to_dict()
    index = data['model']
    print(data)
    print(index)
    if index =='2':
        print("新增")
        insert(data)
    elif index == '3':
        delete(data)
    elif index == '4':
        updata(data)
    else:print("选择有误！")
    list = select()
    return render_template("mysql_wb.html",title = "数据库",data = list)



if __name__ == '__main__':
    app.run(debug=True )