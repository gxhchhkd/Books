#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    python_operator.py
 @Function:    python operator
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/6/19
"""

"""一、运算符概述"""

"""
1、什么是运算符？
    运算符是一种特殊的符号，通过运算符可以对相应数据类型的运算数进行运算
    例如：加法运算符+可以将两个整数类型的运算数进行相加运算，比如 1 + 2
    布尔运算符and可用于将两个布尔类型的运算数进行逻辑与的运算，比如True and False
"""

"""
2、常见的运算符
    (1) 标准算术运算符(+、-、*、/)
    (2) 取余运算符(%)
    (3) 幂运算符
    (4) 布尔运算符
    (5) 比较运算符
    (6) 赋值运算符
"""


"""二、标准算术运算符"""

"""
1、标准算术运算符
    标准算术运算符包括加减乘除四个运算符，分别为：+、-、*、/
    其中，使用*表示数学中的乘号，使用/表示数学中的除号
"""

print(3 + 5)    # 8
print(8 - 2)    # 6
print(5 * 6)    # 30
print(2.8 / 4)  # 0.7

"""
2、整数除运算符//
    当使用整数运算符//对两个数值进行运算时，运算结果只保留整数部分
    整数除运算符//用于计算一个数值是另一个数值的多少倍
"""

print(9 // 4)       # 2
print(5.0 // 2.4)   # 2.0

# 9 = (-4) * (-3) + (-3)
print(9 // -4)  # -3

# -9 = 4 * (-3) + 3
print(-9 // 4)  # -3

# -9 = (-4) * 2 + (-1)
print(-9 // -4) # 2


"""三、取余运算符"""

"""
1、什么是取余运算符？
    取余运算符用%表示
    a % b = a - b * 倍数 = a - b * (a // b) = 余数
    也就是说，a对b取余就是计算a最多可以容纳多少个b，多出来的那部分就是余数
"""
# 9 % 4 = 9 - 4 * (9 // 4) = 1
print(9 % 4)        # 1
print(1.25 % 0.5)   # 0.25

# 9 % -4 = 9 - (-4) * (9 // -4)
print(9 % -4)   # -3
print(-9 % 4)   # 3
print(-9 % -4)  # -1


"""四、幂运算符"""

"""
1、什么是幂运算符？
    幂运算符用于实用幂运算，用两个星号**表示
    内置函数pow也可以实现幂运算
"""

print(3 ** 2)       # 9
print((-3) ** 2)    # 9

print(pow(3, 2))    # 9
print(pow(-3, 2))   # 9


"""五、布尔运算符"""

"""
1、什么是布尔运算符?
    布尔运算符用于对布尔值进行运算，运算结果仍然是一个布尔值
    布尔运算符包含如下三个：
    (1) and
    (2) or
    (3) not
"""

"""
2、布尔运算符and
    当两个运算数都为True时，运算结果才为True
"""

print(True and True)    # True
print(True and False)   # False
print(False and True)   # False
print(False and False)  # False

"""
3、布尔运算符or
    只要有一个运算数为True，运算结果就为True
"""

print(True or True)     # True
print(True or False)    # True
print(False or True)    # True
print(False or False)   # False

"""
4、布尔运算符not
    用于对运算符取反
    (1) 如果运算数为True，运算结果为False
    (2) 如果运算数为False，运算结果为True
"""

print(not True)     # False
print(not False)    # True


"""六、赋值运算符和变量"""

"""
1、什么是赋值运算符以及什么是变量？
    赋值运算符用=表示，=的左边是变量，=的右边是对象
    在python中，一切皆为对象。变量相当于标签
    对于赋值语句：变量 = 对象，相当于给对象贴了一个标签，标签名就是变量名
    
    例如：
        对于赋值语句i = 18
        python会分配一块内存空间用于存储整数对象18，然后给整数对象18贴上名为i的标签
        之后我们就可以通过名为i的标签访问整数对象18
        
        接下来执行赋值语句i = 23
        python会再分配一块内存空间用于存储整数对象23
        然后相当于把名为i的标签从整数对象18撕下来并贴在整数对象23上
        这样，我们就无法再通过名为i的标签访问整数对象18了
        
        接下来执行赋值语句j = i
        相当于在整数对象23上又贴了一个名为j的标签
        这样，我们既可以通过名为i的标签访问整数对象23，又可以通过名为j的标签访问整数对象23
        
    注意：
        在某一时刻，一个标签只能贴在一个对象上，一个对象上可以贴多个标签
        变量是没有数据类型的，只有对象才有数据类型
        通常情况下，一个变量只引用一种数据类型的对象
"""

i = 18
print(i)    # 18
i = 23
print(i)    # 23

# 变量i引用了另一种数据类型的对象(不推荐)
i = 'Hello'
print(i)    # Hello

"""
2、赋值运算符支持链式赋值
    如果想让多个变量同时引用同一个对象，可以使用链式赋值
"""

a = b = c = 18
print(a)    # 18
print(b)    # 18
print(c)    # 18

"""
3、赋值运算符支持参数赋值
    可以在赋值运算符的左边添加其它运算符，从而实现参数赋值，例如：+=、-=、*=、/=、%=
    a += b 相当于：a = a + b
    a -= b 相当于：a = a - b
    其余类似，参数赋值可以使代码更加简洁，而且可读性更强
"""

a = 3
a += 5
print(a)    # 8
a -= 2
print(a)    # 6
a *= 8
print(a)    # 48
a /= 2
print(a)    # 24.0
a //= 5
print(a)    # 4.0
a %= 3
print(a)    # 1.0


"""七、比较运算符"""

"""
1、什么是比较运算符？
    比较运算符用于比较两个运算数，比较结果是一个布尔值
    比较运算符包括如下几个：
    (1) <、<=
    (2) >、>=
    (3) ==
        ==用于比较两个运算数是否相等，也就是说，==用于"相等性"测试
    (4) !=
    (5) is
        is用于比较两个运算数是否是同一个对象，也就是说，is用于"同一性"测试
    (6) is not
"""

print(6 < 8)        # True
print(6 <= 8)       # True
print(8 > 6)        # True
print(8 >= 6)       # True
print(8 == 8.0)     # True
print(8 != 8.0)     # False

a = b = [1, 2, 3]
c = [1, 2, 3]
print(a == b)   # True
print(a == c)   # True
print(a is b)   # True
print(a is c)   # False

"""
2、不可变类型对象的is比较
    对于不可变类型的对象，其内存可能会被重用，比如数值较小的整数对象
    可以调用内置函数id进行验证。内置函数id用于返回对象的唯一标识(对象在内存中的地址)
"""

a = 18
b = 18
print(id(a))    # 4328201040
print(id(b))    # 4328201040
print(a is b)   # True

"""
3、比较运算符可用于链式比较
"""

age = 18
print(0 < age < 100)    # True
# 以上语句相当于：
# print(0 < age and age < 100)    # True
print(1 == 2 < 3)   # False
# 以上语句相当于：
# print(1 == 2 and 2 < 3) # False


"""八、运算符的优先级和结合性"""

"""
1、什么是运算符的优先级？
    每个运算符都有固定的优先级
    当表达式中包含优先级不同的运算符时，高优先级的运算符先以参与运算
    例如：运算符*和/的优先级比运算符+和-的优先级高，正所谓"先乘除，后加减"
"""

# *比+的优先级高，*先参与运算
print(2 + 3 * 4)    # 14

"""
2、什么是运算符的结合性？
    每个运算符都有固定的结合性
    当表达式中包含优先级相同的运算符时，结合性定义了哪个运算符先参与运算
    
    如果运算符的结合性为左，那么左边的运算符先参与运算
    例如：2 + 3 - 4，2 + 3会先参与运算
    如果运算符的结合性为右，那么右边的运算符先参与运算
    例如：a = b = 18，b = 18会先以参与运算
"""

"""
3、正确使用运算符的优先级和结合性
    没有必要记忆所有运算符的优先级和结合性
    
    对于包含多个运算符的复杂表达式，其可读性是较低的，为了提高可读性，建议的方法有两种：
    (1) 在复杂表达式中使用小括号指定运算顺序
    (2) 将复杂表达式拆分成几步来完成
"""

is_has_key = False
is_entered_door = False
is_passed_scan = False
is_know_password = True

# and比or的优先级高，or的结合性是左
print(is_has_key or is_entered_door and is_passed_scan or is_know_password)     # True
# 在复杂表达式中使用小括号指定运算顺序
print((is_has_key or (is_entered_door and is_passed_scan)) or is_know_password) # True

# 将复杂表达式拆分成几步来完成
step1 = is_entered_door and is_passed_scan
step2 = is_has_key or step1
step3 = step2 or is_know_password
print(step3)    # True


"""九、关键字和标识符"""

"""
1、关键字
    所谓关键字，就是python语言定义的、具有特殊用途的单词
    
    通过内置函数help()查看所有关键字：
    >>> help()
    help> keywords
    
    通过导入模块keyword查看所有关键字：
    >>> import keyword
    >>> keyword.kwlist
"""

"""
2、标识符
    所谓标识符，就是给程序中的变量、函数、方法、类等命名的名字
    
    标识符的命名规则(必须这样命名)：
    (1) 区分大小写
    (2) 不能是关键字
    (3) 不能以数字开头
    (4) 不能包含空格、制表符、数学符号、中划线、箭头等
    
    标识符的命名规范(推荐这样命名):
    (1) "见名知意"，由一个或多个有意义的单词组合而成
    (2) 所有单词全部小写，单词之间用下划线进行分隔
    例如：student_name，return_result
"""

i = 3
I = 5
print(i)    # 3
print(I)    # 5

# 标识符不能是关键字
# True = 8

# 标识符不能以数字开头
# 5i = 18

# 标识符不能包含空格
# i 5 = 18

# 标识符不能包含制表符
# i   5= 18

# 标识符不能包含数学符号
# i+5 = 18
# i*5 = 18

# 标识符不能包含中划线
# i-5 = 18

# 标识符不能包含箭头
# i↑5 = 18


"""十、多个变量同时赋值"""

"""
1、赋值运算符的左边可以是一个所有元素都为变量的元组或列表，从而一次给多个变量同时赋值
"""

# a, b = [5, 8]
[a, b] = [5, 8]
print(a, b) # 5 8

a, b = 5, 8
# [a, b] = [5, 8]
print(a, b) # 5 8

"""
2、赋值运算符左右两边的元素个数必须是相同的，否则会抛出ValueError
"""
# a, b = 5, 8, 3  # ValueError: too many values to unpack (expected 2)

"""
3、可以在赋值运算符左边的某个变量前添加*，以匹配赋值运算符右边的0个或多个元素
"""

a, *b, c = 1, 2, 3, 4
print(a, b, c)  # 1 [2, 3] 4

a, b, *c = 1, 2, 3, 4
print(a, b, c)  # 1 2 [3, 4]

*a, b, c = 1, 2, 3, 4
print(a, b, c)  # [1, 2] 3 4

a, *b, c = 1, 2
print(a, b, c)  # 1 [] 2

"""
4、交换两个变量的值
"""

"""
a = 5
b = 8

temp = a
a = b
b = temp

print(a, b) # 8 5
"""

# 赋值运算符的左右两边都是元组，左边是变量的元组，右边是表达式的元组
# 先将右边的所有表达式都计算完之后，再分别赋值给左边的所有变量
a = 5
b = 8
a, b = b, a
print(a, b) # 8 5