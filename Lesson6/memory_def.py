from __future__ import print_function
from sys import getsizeof, stderr
from itertools import chain
from collections import deque
import sys

def total_size(o, handlers={}, verbose=False):
    """ Возвращает приблизительный объем памяти для объекта и всего содержимого.
    Автоматически находит содержимое следующих встроенных контейнеров и
    их подклассы: кортеж, список, deque, dict, set и frozenset.
    Чтобы выполнить поиск в других контейнерах, добавьте обработчики для перебора их содержимого.
    """
    dict_handler = lambda d: chain.from_iterable(d.items())
    all_handlers = {tuple: iter,
                    list: iter,
                    deque: iter,
                    dict: dict_handler,
                    set: iter,
                    frozenset: iter,
                   }
    all_handlers.update(handlers)     # обработчики пользователей имеют приоритет
    default_size = getsizeof(0)       # оценка размера памяти объекта

    def sizeof(o):
        s = getsizeof(o, default_size)

        if verbose:                                 # расчитывает память для всего содержимого объекта
            print(s, type(o), repr(o), file=stderr)

        for typ, handler in all_handlers.items():
            if isinstance(o, typ):
                s += sum(map(sizeof, handler(o)))
                break
        return s

    return sizeof(o)

def show_size(x, level=0):
    print('\t' * level, f'type = {x.__class__}, size = {sys.getsizeof(x)}, object = {x}')

    if hasattr(x, '__iter__'):

        if hasattr(x, 'items'):
            for xx in x.items():
                show_size(xx, level + 1)

        elif not isinstance(x, str):
            for xx in x:
                show_size(xx, level + 1)