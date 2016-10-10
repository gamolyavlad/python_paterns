"""
The memento pattern is a software design pattern that provides the ability to restore an object to its previous state
(undo via rollback)
"""


class MementoMetaclass(type):
    cache = {}

    def __call__(self, *args):
        print("=" * 20)
        print("ClassObj:", self)
        print("Args:", args)
        print("=" * 20)
        cached = self.cache.get(args, None)
        if not cached:
            instance = type.__call__(self, *args)
            self.cache.update({args: instance})
            return instance
        return cached


class Foo(object):
    __metaclass__ = MementoMetaclass
    template = ''

    def __init__(self, arg1, arg2, arg3):
        self.template = arg1


if __name__ == '__main__':
    a = Foo(1, 2, 3)
    b = Foo(2, 3, 4)
    c = Foo(1, 2, 3)
    d = Foo(2, 3, 4)
    e = Foo(5, 6, 7)
    f = Foo(5, 6, 7)

    print(id(a), id(b), id(c), id(d), id(e), id(f))
# from copy import copy, deepcopy
#
#
# def memento(obj, deep=False):
#     state = deepcopy(obj.__dict__) if deep else copy(obj.__dict__)
#
#     def restore():
#         obj.__dict__.clear()
#         obj.__dict__.update(state)
#
#     return restore
#
#
# class Transaction:
#     """A transaction guard.
#     This is, in fact, just syntactic sugar around a memento closure.
#     """
#     deep = False
#     states = []
#
#     def __init__(self, deep, *targets):
#         self.deep = deep
#         self.targets = targets
#         self.commit()
#
#     def commit(self):
#         self.states = [memento(target, self.deep) for target in self.targets]
#
#     def rollback(self):
#         for a_state in self.states:
#             a_state()
#
#
# class Transactional(object):
#     """Adds transactional semantics to methods. Methods decorated  with
#     @Transactional will rollback to entry-state upon exceptions.
#     """
#
#     def __init__(self, method):
#         self.method = method
#
#     def __get__(self, obj, T):
#         def transaction(*args, **kwargs):
#             state = memento(obj)
#             try:
#                 return self.method(obj, *args, **kwargs)
#             except Exception as e:
#                 state()
#                 raise e
#
#         return transaction
#
#
# class NumObj(object):
#     def __init__(self, value):
#         self.value = value
#
#     def __repr__(self):
#         return '<%s: %r>' % (self.__class__.__name__, self.value)
#
#     def increment(self):
#         self.value += 1
#
#     @Transactional
#     def do_stuff(self):
#         self.value = '1111'  # <- invalid value
#         self.increment()  # <- will fail and rollback
#
#
# if __name__ == '__main__':
#     num_obj = NumObj(-1)
#     print(num_obj)
#
#     a_transaction = Transaction(True, num_obj)
#     try:
#         for i in range(3):
#             num_obj.increment()
#             print(num_obj)
#         a_transaction.commit()
#         print('-- committed')
#
#         for i in range(3):
#             num_obj.increment()
#             print(num_obj)
#         num_obj.value += 'x'  # will fail
#         print(num_obj)
#     except Exception as e:
#         a_transaction.rollback()
#         print('-- rolled back')
#     print(num_obj)
#
#     print('-- now doing stuff ...')
#     try:
#         num_obj.do_stuff()
#     except Exception as e:
#         print('-> doing stuff failed!')
#         import sys
#         import traceback
#
#         traceback.print_exc(file=sys.stdout)
#     print(num_obj)
