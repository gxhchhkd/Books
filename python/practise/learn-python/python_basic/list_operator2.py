#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    list_operator2.py
 @Function:    python list operator
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/6/23
"""

"""一、使用加法和乘法运算符操作列表"""

"""
1、使用加法运算符操作列表
    可以使用加法运算符将两个列表合并后生成一个新列表，被合并的两个列表不发生任何变化
"""

L1 = [1, 2, 3]
L2 = [4, 5, 6]
L3 = L1 + L2
print(L3)   # [1, 2, 3, 4, 5, 6]
print(L1)   # [1, 2, 3]
print(L2)   # [1, 2, 3]

L1 = L2 = [1, 2]
L1 = L1 + [3, 4]
print(L1, L2)   # [1, 2, 3, 4] [1, 2]

# 参数赋值运算符+=会对列表本身进行修改
L1 = L2 = [1, 2]
L1 += [3, 4]
print(L1, L2)   # [1, 2, 3, 4] [1, 2, 3, 4]

"""
2、使用乘法运算符操作列表
    可以使用乘法运算符将列表中的所有元素重复n次后生成一个新列表，被乘的列表不发生任何变化
"""

L1 = [1, 2, 3]
L = L1 * 3
print(L)        # [1, 2, 3, 1, 2, 3, 1, 2, 3]
print(L1)       # [1, 2, 3]

# 常用于列表的初始化
L = [0] * 5
print(L)        # [0, 0, 0, 0, 0]

L1 = L2 = [1, 2]
L1 = L1 * 3
print(L1, L2)   # [1, 2, 1, 2, 1, 2] [1, 2]

# 参数赋值运算符*=会对列表本身进行修改
L1 = L2 = [1, 2]
L1 *= 3
print(L1, L2)   # [1, 2, 1, 2, 1, 2] [1, 2, 1, 2, 1, 2]


"""二、使用比较运算符比较两个列表"""

"""
可以使用如下的比较运算符对两个列表进行比较：
    >、>=、<、<=、==、!=
比较规则为：
    首先比较两个列表中的第一个元素，如果相等则继续比较下一个元素，依次比较下去，
直到两个列表中的元素不相等时其比较结果就是两个列表的比较结果，两个列表中的所有后续元素将
不再被比较
"""

print([2, 3, 8, 6, 7] < [2, 3, 9, 5, 1])    # True
print([7, [2, 6]] > [7, [2, 5]])    # True

"""
    还可以使用is对两个列表进行比较。
    ==与is的区别：==是"相等性"测试，is是"同一性"测试。
"""

a = b = [1, 2, 3]
c = [1, 2, 3]

print(a == b)   # True
print(a == c)   # True

print(a is b)   # True
print(a is c)   # False