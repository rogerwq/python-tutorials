def check_types():
    a = 1
    b = 'hello'
    c = []
    d = {}
    print(f'type of int: {type(a)}')
    print(f'type of str: {type(b)}')
    print(f'type of list: {type(c)}')
    print(f'type of dict: {type(d)}')

    class E:
        pass
    print(f'type of class E: {type(E)}')
    print(f'type of class type: {type(type)}')

def first_metaclass():
    # class A:
    #     pass

    # # not any class can be metaclass
    # class B(metaclass=A):
    #     pass

    from abc import ABCMeta

    class C(metaclass=ABCMeta):
        pass
    print(f'type of class C: {type(C)}')

    class D(C):
        pass 
    print(f'type of class D: {type(D)}')

    class E(D):
        pass
    print(f'type of class E: {type(E)}')

def main():
    check_types()
    first_metaclass()

if __name__ == "__main__":
    main()