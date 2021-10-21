# 异常处理
# Python 用异常对象（exception object）来表示异常情况。
# 当程序在运行过程中遇到错误时，会引发异常。如果异常对象未被处理或捕捉，程序就会用所谓的回溯（Traceback，一种错误信息）终止执行
# 可以通过 try/except 来捕捉异常，可以使用多个 except 子句来分别处理不同的异常。
# else 子句在主 try 块没有引发异常的情况下被执行。
# finally 子句不管是否发生异常都会被执行。
# 通过继承 Exception 类可以创建自己的异常类。
import datetime

print(datetime.datetime.now())
print(datetime.timedelta(days=7))
print((datetime.datetime.now() - datetime.timedelta(days=7)).strftime('%Y.%m.%d'))
