
import os

path = os.path.join( "icon")
print(path)
print(os.listdir(path))


file = open("test.txt","ab")


while True:
    out = input("输出")
    if out == "q":
        break
    #out = out+'\n'
    out = "{}\n".format(out)
    file.write(out.encode("utf-8"))

file.close()

file = open("test.txt","rb")

txt = file.read()
txt = txt.decode("utf-8")
txt = txt.strip().split("\n")
print(txt)

file.close()

with open("test.txt","rb") as f:
    data = f.read()
    data = data.decode("utf-8")
    data = data.strip().split("\n")
    print(data)

