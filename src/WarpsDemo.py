import time
from functools import wraps
import random


def decorator_func_no_param(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print "decorator_func_no_param wrapper function=" + func.__name__
        print "function " + func.__name__ + ' start exec'
        start = long(time.time())
        time.sleep(random.randint(1, 3))
        result = func(*args, **kwargs)
        end = long(time.time())
        print 'function %s end exec, cost time=%s' % (func.__name__, (end - start))
        return result

    return wrapper


def decorator_func_with_param(param1):
    '''
    带有参数的装饰器函数，通过外边包一层，来让传入函数
    :param param1:
    :return:
    '''
    def outer(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print "decorator_func_with_param wrapper function=" + func.__name__
            print "logger2 param1=%s" % param1
            print "function " + func.__name__ + ' start exec'
            start = long(time.time())
            time.sleep(random.randint(1, 3))
            result = func(*args, **kwargs)
            end = long(time.time())
            print 'function %s end exec, cost time=%s' % (func.__name__, (end - start))
            return result

        return wrapper

    return outer


class DecoratorNoParamClass(object):
    def __init__(self, func):
        self._func = func

    def __call__(self, *args, **kwargs):
        print "DecoratorNoParamClass wrapper function=" + self._func.__name__
        return self._func(*args, **kwargs)


class DecoratorWithParamClass(object):
    '''
    带有参数的装饰器类，不会像不带参数的一样__init__传入的是被装饰的函数，而是传入的装饰器类参数
    被装饰的函数通过__call__传入，所有跟没有参数的装饰器类差别较大
    '''
    def __init__(self, param):
        self.param = param

    def __call__(self, func):
        def __call__(*args, **kwargs):
            print "DecoratorWithParamClass wrapper function=" + func.__name__
            return func(*args, **kwargs)

        return __call__


@decorator_func_no_param
def foo(name=None):
    print "foo"


@decorator_func_with_param("param1")
def foo2(name=None):
    print "foo2"


@DecoratorNoParamClass
def foo3(name=None):
    if not name:
        name = "default_name"
    print "hello: " + name


@DecoratorWithParamClass(param="classParam")
def foo4(name=None):
    if not name:
        name = "default_name"
    print "hello: " + name


if __name__ == "__main__":
    foo("foo")
    foo2("foo2")
    foo3("foo3")
    foo4("foo4")
