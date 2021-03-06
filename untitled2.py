# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1B_6-y1IOweCnsUDgVMoqSuWGK-v0pucV

**HEAPQ**

https://docs.python.org/3/library/heapq.html


Структура данных кучи в основном используется для представления очереди с приоритетами. 

Операции на куче:

1. heapify (итерируемый) : — эта функция используется для преобразования итерируемого в структуру данных кучи . т.е. в порядке кучи.

2. heappush (heap, ele) : — Эта функция используется для вставки элемента, упомянутого в его аргументах, в кучу. Порядок корректируется , так что структура кучи сохраняется .

3. heappop (heap) : — эта функция используется для удаления и возврата наименьшего элемента из кучи. Порядок корректируется , так что структура кучи сохраняется .
"""

import heapq


ls = [8, 2, 0, 7, 0.5]

heapq.heapify(ls)   # преобразование списка в кучу

print ("heap0 : ", list(ls))

heapq.heappush(ls, 4)  # вставки элемента в кучу

print ("heap1 : ", list(ls))

print ("heap2 : ", heapq.heappop(ls))  # вывод наименьшего элемента

print (ls1)

"""4. heappushpop (heap, ele) : — Эта функция объединяет функции операций push и pop в одном операторе, повышая эффективность. Порядок кучи сохраняется после этой операции.

5. heapreplace (heap, ele) : — Эта функция также объединяет функции операций push и pop, но при этом сначала извлекается элемент, а затем добавляется новый.
"""

import heapq

ls1 = [8, 2, 9, 7, 0.5]

ls2 = [8, 2, 9, 7, 0.5]

heapq.heapify(ls1)
heapq.heapify(ls2)

print ("heap3 : ", heapq.heappushpop(ls1, 0.3))
print (ls1)

print ("heap4 : ",heapq.heapreplace(ls2, 0.3))
print(ls2)

"""6. nlargest (k, iterable, key = fun) : — Эта функция используется для возврата k наибольших элементов из указанной повторяемой и удовлетворяющих ключу, если упомянуто.

7. nsmallest (k, iterable, key = fun) : — Эта функция используется для возврата k наименьших элементов из указанного повторяемого и удовлетворяющего ключу, если упомянуто.
"""

import heapq

ls1 = [6, 7, 9, 4, 3, 5, 8, 10, 1]
ls = ['B', 'C', 'D', 'E', 'a', 't', 's']

heapq.heapify(ls1)
heapq.heapify(ls)

print("heap5 : ", heapq.nlargest(3, ls1))  # вывод 3 самых больших чисел

print(ls1)

print("heap5_2 : ", heapq.nlargest(3, ls, key=str.lower))

print("heap6 : ", heapq.nsmallest(3, ls1))  # вывод 3 самых маленьких чисел

print(ls1)

"""**Задание**: создать кучу из 10 случайных чисел и вывести наименьшие числа с 4 по 6 (порядковые номера изначальной **кучу**)

---
**BISECT**

https://pythonworld.ru/moduli/modul-bisect.html

Модуль bisect - обеспечивает поддержку списка в отсортированном порядке с помощью алгоритма деления пополам.

Набор функций:

bisect.insort(list, elem), он же bisect.insort_right(list, elem) - вставка элемента в отсортированный список, при этом elem располагается как можно правее (все элементы, равные ему, остаются слева).

bisect.insort_left(list, elem) - вставка элемента в отсортированный список, при этом elem располагается как можно левее (все элементы, равные ему, остаются справа).

bisect.bisect(list, elem), он же bisect.bisect_right(list, elem) - поиск места для вставки элемента в отсортированный список, таким образом, чтобы elem располагался как можно правее.

bisect.bisect_left(list, elem) - поиск места для вставки элемента в отсортированный список, таким образом, чтобы elem располагался как можно левее.
"""

import bisect

ls = [1,5,7,8,9,11]

bisect.insort(ls, 2)
print('ls1 : ', ls)

pos = bisect.bisect(ls, 3)
print('position : ', pos)

"""**Задание:** создать отсортированный список из 10 элементов, ввести некоторое чисто а. Найти позицию а, если вставлять его в список как можно правее, а затем добавить его в список как можно левее.

---
**QUEUE**

https://docs.python.org/3/library/queue.html

Модуль Queue реализует механизм очереди. Он особенно полезен в многопоточном программировании, когда необходимо безопасно передавать информацию между потоками.

**Типы очередей**
Модуль предоставляет реализации трех типов очередей, единственная разница которых это порядок получаемых значений.

class Queue.Queue(maxsize)
Класс, реализующий очередь FIFO (First Input First Output - первым вошел, первым вышел). maxsize - параметр типа integer, который устанавливает предел для числа элементов, которые могут быть помещены в очередь. Вставка новых элементов блокируется, как только этот размер был достигнут, до тех пор пока элементы не будут удалены из очереди. Если значение параметра равно или меньше нуля, то очередь будет бесконечной.

class Queue.LifoQueue(maxsize)
Класс реализующий очередь LIFO, или по другому "стэк"(Last Input First Output - последним вошел, первым вышел). Параметр maxsize аналогичен параметру в классе Queue.Queue.

class Queue.PriorityQueue(maxsize)
Класс реализующий очередь с приоритетами. Параметр maxsize аналогичен параметру в классе Queue.Queue.

Элементы, добавляемые в подобную очередь, должны представлять из себя кортеж типа (значение приоритета, данные). Первыми из очереди забираются элементы с меньшим приоритетом, полученным с помощью функции sorted().
"""

import queue

q = queue.Queue()

for i in range(5):
    q.put(i)

while not q.empty():
    print(q.get())

"""**Исключения**
В модуле определены следующие исключения:

exception Queue.Empty
Возникает, когда вызывается не блокирующий метод get() (или get_nowait()) пустого объекта Queue.

exception Queue.Full
Возникает, когда вызывается не блокирующий метод put() (или put_nowait()) заполненного объекта Queue.

**Методы объектов**

Queue.qsize()
Возвращаем аппроксимированный размер очереди. Однако, qsize()>0 не гарантирует, что последующий get() не будет блокирован, и также qsize()<maxsize не будет гарантировать что put() не будет блокирован.

Queue.empty()
Возвращает True если очередь пуста, False в противном случае. Однако если метод возвращает True не гарантируется что следующий вызов put() не будет блокирован. Также если возвращает False не гарантируется что последующий get() не будет блокирован.

Queue.full()
Возвращает True если очередь заполнена, False в противном случае. Однако если метод возвращает True не гарантируется что следующий вызов get() не будет блокирован. Также если возвращает False не гарантируется что последующий put() не будет блокирован.

Queue.put(item, [block[, timeout]])
Помещает объект item в очередь. Если block=True и timeout не задан (None по умолчанию), то при необходимости произойдет блокировка до тех пор пока в очереди не будет доступного места. Если timeout это положительное число, то произойдет блокировка на заданное число секунд и будет возбужденно исключение Queue.Full, если в течении этого времени не освободится место в очереди. В другом случае (если block=False), метод помещает объект item в очередь если свободное место доступно немедленно, иначе генерирует исключение Queue.Full (параметр timeout в этом случае игнорируется).

Queue.put_nowait(item)
Эквивалент вызову put(item, False)

Queue.get([block, [timeout]])
Удалить и возвратить элемент из очереди. Если block=True и timeout не задан (None по умолчанию), произойдет блокировка до тех пор пока элемент не будет доступен. Если timeout это положительное число, то произойдет блокировка на заданное число секунд и будет возбужденно исключение Queue.Empty если в течении этого времени элемент не будет дсотупен. В другом случае (если block=False), метод возвращает элемент очереди немедленно, иначе генерирует исключение Queue.Empty (параметр timeout в этом случае игнорируется).

Queue.get_nowait()
Эквивалент вызову get(False).


Следующие два метода предлагаются для поддержки и отслеживания были ли ставшие в очередь задачи полностью обработаны потребительскими потоками.

Queue.task_done()
Сообщает что ранее полученное задание из очереди выполнено. Используется потребительскими потоками. Для каждого вызова get() последующий вызов task_done() сообщает объекту очереди что обработка задания завершена.
Если количество вызовов task_done() превзойдет количество вызовов put(), то будет вызвано исключение ValueError.

Queue.join()
Вызов блокировки до тех пор, пока все элементы из очереди не будут полученны и обработаны.
Количество не выполненных заданий возрастает тогда, когда добавляются элементы в очередь, а уменьшается когда потребительский поток вызывает task_done().
Если join() находится в заблокировано состоянии, то это означает, что количество вызванных put() не соответствует количеству вызванных task_done() и задания из очереди не обработаны. Блокировка снимется тогда когда количество вызовов сравняется.
"""

import queue

q = queue.Queue()

for i in range(5):
    q.put(i)

print('size : ', q.qsize())
print('fullness : ', q.full())

q.put(9)
while not q.empty():
    print(q.get())

"""**Задание:** создать очередь с приоритетом из 3 элементов, вывести ее. Затем добавить еще один элемент и вывести конечный вариант очереди."""