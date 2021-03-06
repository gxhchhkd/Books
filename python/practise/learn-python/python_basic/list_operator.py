#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    list_operator.py
 @Function:    python list operator
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/6/22
"""

"""一、列表的"改"操作"""

"""
1、修改列表元素
    如果想要修改列表中的元素，有两种常见的方式：
    (1) 为指定索引的元素赋予一个新值(一次只修改一个元素)
    (2) 为指定的切片赋予一个新值(一次至少修改一个元素)
"""

L= [3, 4, 5, 6, 7]

L[2] = 8
print(L)    # [3, 4, 8, 6, 7]

L[1:4] = [1, 9, 2]
print(L)    # [3, 1, 9, 2, 7]

L[1:2] = [5]
print(L)    # [3, 5, 9, 2, 7]

# 等号左右的元素个数可以不同。此时，列表中其它元素的索引也会随之改变
L[1:4] = [1, 8]
print(L)    # [3, 1, 8, 7]


"""二、列表的"增"操作"""

"""
如果想往列表中添加元素，有四种常见的方式：
1、调用方法append(在列表的末尾一次只添加一个元素)
"""

L = [3, 4, 5, 6, 7]

L.append(8)
print(L)    # [3, 4, 5, 6, 7, 8]

L.append([9, 10])
print(L)    # [3, 4, 5, 6, 7, 8, [9, 10]]

"""
2、调用方法extend(在列表的末尾一次至少添加一个元素)
    将参数中的所有元素依次添加到列表的末尾
"""

L = [3, 4, 5, 6, 7, 8]

L.extend([9, 10])
print(L)    # [3, 4, 5, 6, 7, 8, 9, 10]

"""
3、调用方法insert(在列表的任意位置一次只添加一个元素)
    第1个参数指定插入位置，第2个参数指定被插入的元素
    插入位置后面的所有元素依次后移一个位置
"""

L = [3, 4, 5, 6, 7]

L.insert(3, 8)
print(L)    # [3, 4, 5, 8, 6, 7]

# 调用内置函数len可以获取列表中的元素个数
L.insert(len(L), 9)
print(L)    # [3, 4, 5, 8, 6, 7, 9]

"""
4、为指定的切片赋予一个新值(在列表的任意位置一次至少添加一个元素)
"""

L = [3, 4, 5, 6]

# 与列表的"改"操作结合对比学习更容易理解
L[2:2] = [8, 9]
print(L)    # [3, 4, 8, 9, 5, 6]

L[len(L):] = [1, 2]
print(L)    # [3, 4, 8, 9, 5, 6, 1, 2]


"""三、列表的"删"操作"""

"""
如果想要删除列表中的元素，有五种常见的方式：
1、调用方法remove(一次只删除一个指定的元素)
    被删除元素后面的所有元素依次前移一个位置
"""

L = [3, 4, 5, 6, 5, 7]

L.remove(4)
print(L)    # [3, 5, 6, 5, 7]

# 如果列表中存在多个指定元素，只删除第1个指定元素
L.remove(5)
print(L)    # [3, 6, 5, 7]

# 如果要删除的指定元素在列表中不存在，抛出ValueError
# L.remove(8) # ValueError: list.remove(x): x not in list

"""
2、调用方法pop(一次只删除一个指定索引的元素)
    该方法返回被删除的元素
"""

L = [3, 4, 5, 6, 7]

print(L.pop(2)) # 5
print(L)        # [3, 4, 6, 7]

# 如果指定的索引不存在，抛出IndexError
# L.pop(8)        # IndexError: pop index out of range

# 如果没有指定索引，默认删除列表中的最后一个元素
print(L.pop())  # 7
print(L)        # [3, 4, 6]

"""
3、使用del语句(一次至少删除一个元素)
"""

L = [3, 4, 5, 6, 7, 8, 9]

del L[2]
print(L)    # [3, 4, 6, 7, 8, 9]

del L[1:4]
print(L)    # [3, 8, 9]

"""
4、给指定的切片赋值一个空列表(一次至少删除一个元素)
"""

L = [3, 4, 5, 6, 7, 8, 9]

L[2:3] = []
print(L)    # [3, 4, 6, 7, 8, 9]

L[1:4] = []
print(L)    # [3, 8, 9]

# 清空列表
L[:] = []
print(L)    # []

"""
5、调用方法clear清空列表
"""

L = [3, 4, 5, 6, 7]

L.clear()
print(L)    # []
