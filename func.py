

#正则表达式
import re
text = "xulei 的qq邮箱是5555556@qq.com,手机号是17640628666"
#固定字符
print(re.findall("xulei", text))
#匹配字符 加【】 表示其中任意一个都可以
print(re.findall("[xulei]", text))
#字符的范围  a-z 0-9
print(re.findall("[0-5]", text))
#\d代表一个数字
print(re.findall("\d@", text))
#+ 代表出现一遍到n遍
print(re.findall("\d+@", text))
#*代表出现0遍到n遍
print(re.findall("\d*@", text))
#?代表出现0遍到1遍
print(re.findall("\d?@", text))
#{2}代表出现2遍
print(re.findall("\d{2}@", text))
#{2,}代表出现2遍以上
print(re.findall("x{2,}@", text))
#\w代表字母数字下划线中文  尽可能多的匹配
print(re.findall("是+\w", text))
#\w+?代表字母数字下划线中文  尽可能少的匹配  就是在数量后面加一个？变成非贪婪
print(re.findall("是\w+?", text))

#.除换行符的任意字符 要是像表示.这个字符就\.表示
print(re.findall("邮箱是.+com", text))

#\s  代表空格
print(re.findall("i\w*\s\w+", text))


#match 代表从头匹配 返回第一个  search就是纵观文档匹配 返回第一个
s = re.match("i\w*\s\w+", text)
s = s.group()
s = re.search("i\w*\s\w+", text)
s = s.group()
#^  $ 必须是在这两个符号之内的 在多就返回none  限制字符串与正则一模一样
print(re.match("^i\w*\s\w+$", text))
#分割
print(re.split("是", text))

def a():
    print("a")
def b():
    print("b")
def c():
    print("c")
fun = [a,b,c]
fun[0]()#可以指定运行那个函数


a= 1
b = 2
print(lambda a,b:a+b)
print(a if a<b else b)
print([x * x for x in range(1, 11)])

import hashlib
#加密 不可以反解
salt = "ssssss"  #加盐
data = "xulei"
obj = hashlib.md5(salt.encode("utf-8"))
obj.update(data.encode("utf-8"))
print(obj.hexdigest())

import json
#存储格式 目的是让不同语言的数据相互传输
date = "xulei"
res = json.dumps(date)#序列化
print(res)

res = json.loads(res)#反序
print(res)

import decimal

import  time
#获取时间戳
print(time.time())
#延时 秒
time.sleep(5)
import datetime
print(datetime.datetime.now())
date = datetime.datetime.now()
strtinme = date.strftime("%Y-%m-%d %H:%M:%S ")
print(strtinme)

import os
#根据不同系统生成路径
path = os.path.join("x1","x2","x3","x4","x5","x6")
print(path)
#找到上级目录
path = os.path.dirname(path)
print(path)
#生成绝对路径
path = os.path.abspath("")
print(path)
#判断路径存在
print(os.path.exists(path))
#创建文件夹
#os.makedirs("icon")
#删除文件
#os.remove("")

