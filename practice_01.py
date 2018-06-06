#!/usr/bin/python3

# Python3 基本数据类型

# 1. 整型变量，浮点型变量，字符串
counter = 100
miles = 1000.0
name = "runoob"

print(counter)
print(miles)
print(name)

# 2. 在Python 3里，只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
# 内置的 type() 函数可以用来查询变量所指的对象类型
print('----------------------------')

print(type(counter))
print(type(miles))
print(type(name))

# 3. 字符串截取
# 索引值以 0 为开始值，-1 为从末尾的开始位置。是左闭右开区间，包含左边字符，不包含右边
# 字符串可以用+运算符连接在一起，用*运算符重复
print('----------------------------')

str = 'Runoob'

print(str)  # 输出字符串
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str[0])  # 输出字符串第一个字符
print(str[2:5])  # 输出从第三个开始到第五个的字符
print(str[2:])  # 输出从第三个开始的后的所有字符
print(str * 2)  # 输出字符串两次
print(str + "TEST")  # 连接字符串
print(str * 2)  # 重复

# 4. list 列表 []
# list 中的元素可以是不同类型的,可重复的
# List 中的元素是可以改变的
print('----------------------------')

list = ['abcd', 786, 2.23, 'runoob', 70.2, 70.2]
tinylist = [123, 'runoob']

print(list)  # 输出完整列表
print(list[0])  # 输出列表第一个元素
print(list[1:3])  # 从第二个开始输出到第三个元素
print(list[2:])  # 输出从第三个元素开始的所有元素
print(tinylist * 2)  # 输出两次列表
print(list + tinylist)  # 连接列表

list[0] = 1  # 改变 list 中的元素
print(list)

# 5. Tuple 元组 ()
# 元组的元素可重复
# 元组的元素不能修改
# 构造包含0或1个元素的元组的特殊语法规则
print('----------------------------')

tuple = ('abcd', 786, 2.23, 'runoob', 70.2, 70.2)
tinytuple = (123, 'runoob')

print(tuple)  # 输出完整元组
print(tuple[0])  # 输出元组的第一个元素
print(tuple[1:3])  # 输出从第二个元素开始到第三个元素
print(tuple[2:])  # 输出从第三个元素开始的所有元素
print(tinytuple * 2)  # 输出两次元组
print(tuple + tinytuple)  # 连接元组

tup1 = ()  # 空元组
tup2 = (20,)  # 一个元素，需要在元素后添加逗号
print(tup1)
print(tup2)

# 6. Set 集合 {}
# 集合（set）是一个无序不重复元素的序列，基本功能是进行成员关系测试和删除重复元素
# 可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典
print('----------------------------')

student = {'Tom', 'Tom', 'Jim', 'Mary', 'Jack', 'Rose'}

print(student)  # 输出集合，重复的元素被自动去掉

# 成员测试
if ('Rose' in student):
    print('Rose 在集合中')
else:
    print('Rose 不在集合中')

# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a)
print(a - b)  # a和b的差集
print(a | b)  # a和b的并集
print(a & b)  # a和b的交集
print(a ^ b)  # a和b中不同时存在的元素

# 7. Dictionary 字典
# 字典是一种映射类型，它的元素是键值对。
# 字典的关键字必须为不可变类型，且不能重复。
# 创建空字典使用 { }。
print('----------------------------')

dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2] = "2 - 菜鸟工具"

tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}

print(dict['one'])  # 输出键为 'one' 的值
print(dict[2])  # 输出键为 2 的值
print(tinydict)  # 输出完整的字典
print(tinydict.keys())  # 输出所有键
print(tinydict.values())  # 输出所有值

# 8. Python 数据类型转换
# int(x) 将x转换为一个整数
# float(x) 将x转换到一个浮点数
# str(x) 将对象 x 转换为字符串
# tuple(s) 将序列 s 转换为一个元组
# list(s) 将序列 s 转换为一个列表
# set(s) 转换为可变集合
# dict(d) 创建一个字典。d 必须是一个序列 (key,value)元组。




