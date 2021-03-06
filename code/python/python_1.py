'''
参考课程：Python程序设计-浙江大学(https://www.icourse163.org/course/ZJU-1206456840)
'''
'''
0.Python是一种解释型脚本语言
1.标识符是由字母、下划线和数字组成，且不能以数字开头，不能是关键字或内置函数名
2.用type()可以打印出变量的类型
3.变量名是大小写敏感的
4.变量是将名字和对象(如整形、字符串、列表)进行关联
5.id()是Python的内置函数，可以显示对象的地址
    5.1 这和其他语言不太一样（如c）
    5.2 如下所示：x和y的地址一样 都和'test'地址一样
    5.3 这是因为x和y同样都指向'test' 
'''
'''
print('----------------------------------')
x = 'test'
y = 'test'
print(type(x))
print(id(x))
print(id(y))
print(id('test'))
a = 1000
b = 1000
print(id(a))
print(id(b))
print(id(1000))
print('----------------------------------')
'''

'''
1.输入函数input()
    1.1 从标准输入（键盘）中读入一个字符串（注意是字符串）
    1.2 像输入如整形值，则需要强制类型转换
    1.3 想输入多个值，需要使用split()
        1.3.1 对输入有要求如输入1,3可以：a,b = input().split(',')
    1.4 input("请输入")可以加入输入提示语
2.输出函数print()
    2.1 默认输出换行符
    2.2 若想不换行 则print(x, end = '')  
    2.3 end参数可以是空格或者任意的符合
'''
x = int(input("请输入1个整形值："))
print(x, end = '')
print(type(x))
a, b = input("请输入2个整形值：").split()  #仍然是字符串形式
print('a和b分别是：', a, b, end = '*')
