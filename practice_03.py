#!/usr/bin/python3

# Python3 字符串

var1 = 'hello world'

# 1. 可以通过索引访问字符串中的值
print('-------------1---------------')

print(var1[0:5])
print(var1[6:])

# 2. 字符串运算符
# in / not in 是否存在字符串内
print('-------------2---------------')
var_temp = 'hello'
if var_temp in var1:
    print('in')
else:
    print('not in')

# 3. 字符串格式化 %
# %s 格式化字符串；%d 格式化整数； %f 格式化浮点数字，可指定小数点后的精度
print('-------------3---------------')
print('我叫 %s ,今年 %d 岁！' % ('小明', 25))
