# About __call__
#
#   1. 那些对象有__call__这个属性? 可调用callable?
#   2. 如果一个对象不能被调用，如何通过__call__来让它变得可调用？
#   3. __init__() 和 __call__() 有什么区别？
#   4. __call__ 如何在代码中应用？

from typing import Any


def taste_callable():
    a = 1
    assert '__add__' in dir(a)
    assert '__call__' not in dir(a)
    assert not callable(a)

    def foo():
        pass
    assert '__call__' in dir(foo)
    assert callable(foo)

    class A:
        pass
    assert '__call__' not in dir(A)
    assert '__init__' in dir(A)
    A()
    assert callable(A)

    class B:
        pass
        # def __init__(self) -> None:
        #     pass
    B()
    assert '__call__' not in dir(B)
    # 不正确声明： 如果 A(), A 不一定有 __call__ 

def make_object_callalbe():
    class A:
        pass
    a = A()
    # a()
    assert callable(A) 
    assert not callable(a) 

    class B:
        def __call__(self, *args: Any, **kwds: Any) -> Any:
            pass
    b = B()
    b()
    assert callable(b) 

def init_vs_call():
    # __init__ vs __call__
    #   __init__ for class
    #   __call__ for object
    pass

def stateful_method():
    def averge_data_factory():
        data = []
        def average(value):
            data.append(value)
            return sum(data) / len(data)
        return average

    averge_data = averge_data_factory()
    assert averge_data(2) == 2
    assert averge_data(3) == (2 + 3) / 2.0, f'left {averge_data(3)}'
    assert averge_data(4) == (2 + 3 + 4) / 3.0

    class AverageMethod:
        def __init__(self) -> None:
            self.data = []

        def __call__(self, number: Any) -> Any:
            self.data.append(number)
            return sum(self.data) / len(self.data)

    average_method = AverageMethod()
    assert average_method(2) == 2
    assert average_method(3) == (2 + 3) / 2.0
    assert average_method(4) == (2 + 3 + 4) / 3.0

def cache_method():
    # cache
    # from functools import cache
    from time import sleep
    class Factorial:
        def __init__(self) -> None:
            self.cache = {0: 1, 1: 1}

        def __call__(self, num: Any) -> Any:
            if num not in self.cache:
                sleep(1)
                self.cache[num] = num * self(num - 1)
            return self.cache[num]

    factorial = Factorial()
    # assert factorial(0) == 1 # 0! 
    # assert factorial(1) == 1 # 1! 
    # assert factorial(2) == 2 # 2! 
    # assert factorial(3) == 6 # 3! 
    # assert factorial(4) == 24 # 4! 
    # assert factorial(5) == 120 # 5! 

    for i in range(6):
        print(f'{factorial(i)}')
    print(f'{factorial(5)}')
    print(f'{factorial(6)}')
    print(f'{factorial(6)}')
    
def class_decorator():
    import time
    class Timer:
        def __init__(self, func) -> Any:
            self.func = func

        def __call__(self, *args, **kwargs) -> Any:
            start = time.perf_counter() # unit in seconds
            result = self.func(*args, **kwargs)
            end = time.perf_counter()
            print(f'{self.func.__name__} result {result} takes {(end - start) * 1000:.4f} ms')
            return result
        
    class TimerEx:
        def __init__(self, repeat) -> None:
            self.repeat = repeat

        def __call__(self, func) -> Any:
            def timer(*args, **kwargs):
                start = time.perf_counter() # unit in seconds
                for _ in range(self.repeat):
                    result = func(*args, **kwargs)
                end = time.perf_counter()
                print(f'{func.__name__} result {result} takes {(end - start) * 1000:.4f} ms')
                return result
            return timer 

    @Timer
    def square(number):
        return number * number

    @TimerEx(repeat=1000)
    def square_ex(number):
        return number * number
    
    square(2)
    square_ex(2)

def main():
    pass

if __name__ == '__main__':
    main()