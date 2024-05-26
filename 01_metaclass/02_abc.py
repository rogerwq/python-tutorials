def describe_f(f):
    def wrapper():
        print(f'\n# {f.__name__} begin')
        f()
        print(f'# {f.__name__} end')
    return wrapper

@describe_f
def use_abc():
    from abc import ABC, abstractmethod

    class A(ABC):
        @abstractmethod
        def x(self):
            pass

        @abstractmethod
        def y(self):
            pass

    class B(A):
        def x(self):
            pass

        def y(self):
            pass

    b = B()
    print(f'type of class A is {type(A)}')
    print(f'type of class B is {type(B)}')
    print(f'type of b is {type(b)}')

@describe_f
def define_abc():
    def user_abstractmethod(f):
        f.__isabstract__ = True
        return f
    
    def check_abstract_methods(cls):
        visited = []
        errors = []
        while isinstance(cls, UserABCMeta):
            for key, val in vars(cls).items():
                if key in visited:
                    continue
                visited.append(key)

                if getattr(val, '__isabstract__', False):
                    errors.append(key)
            cls = cls.__mro__[1]
        return errors
    
    class UserABCMeta(type):
        def __call__(self, *args, **kwargs):
            errors = check_abstract_methods(self)
            if errors:
                raise TypeError(f'no implementation for method {",".join(errors)}')
            return super().__call__(*args, **kwargs)

    class ABC(metaclass=UserABCMeta):
        pass

    class A(ABC):
        @user_abstractmethod
        def x(self):
            pass

        @user_abstractmethod
        def y(self):
            pass

    class B(A):
        def x(self):
            pass

        def y(self):
            pass

    b = B()
    print(f'type of class A is {type(A)}')
    print(f'type of class B is {type(B)}')
    print(f'type of b is {type(b)}')
    # mro: Method Resolution Order
    print(f'__mro__ of class B: {B.__mro__}')
    print(f'class B is instance of UserABCMeta ? {isinstance(B, UserABCMeta)}')
    print(f'class A is instance of UserABCMeta ? {isinstance(A, UserABCMeta)}')
    print(f'class ABC is instance of UserABCMeta ? {isinstance(ABC, UserABCMeta)}')
    print(f'class object is instance of UserABCMeta ? {isinstance(object, UserABCMeta)}')

def main():
    use_abc()
    define_abc()

if __name__ == "__main__":
    main()