#!/usr/bin/python3

# Python3 控制语句

# 1. input('tip') 输入函数，获取从命令行输入的值，tip 为提示值
print('-------------1---------------')

# var1 = input("name\n")
# print(var1)

# 2. if else
print('-------------2---------------')
var1 = 'hello'
if 'a' in var1:
    print('a in hello')
elif 'b' in var1:
    print('b in hello')
else:
    print('not in')

# 3. while
print('-------------3---------------')
var_int1 = 0
while var_int1 < 3:
    print('var_int1 = ' + str(var_int1))
    var_int1 += 1
print('var_int1 = 3')

# while else
print('--while else--')
var_int2 = 0
while var_int2 < 3:
    print('var_int2 = ' + str(var_int2))
    var_int2 += 1
else:
    print('var_int2 = 3')

# 4. for
# 可以遍历任何序列的项目，如一个列表或者一个字符串
print('-------------4---------------')
languages = ["C", "C++", "Perl", "Python"]
for x in languages:
    print(x)

# 5. range()
# 如果你需要遍历数字序列，可以使用内置range()函数
print('-------------5---------------')
for i in range(5):
    print(i)

# 6 pass 语句
# pass是空语句，是为了保持程序结构的完整性。pass 不做任何事情，一般用做占位语句
print('-------------6---------------')
if 'a' in 'aa':
    pass

