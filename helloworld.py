import os
#print("Hello, World!")
#print (os.path.abspath('.'))
x="/Users/lwd2136/PycharmProjects/test/untitled.txt"
#x = input("请输入：")
for line in open(x):
#for line in x:
    # 去掉左侧空格
    line = line.lstrip()
    # 去掉结尾换行符
    line = line.strip('\n')
    line = line+","+"Netflix"
    print(line)

