"""
Дана строка. Удалите из этой строки все символы @.


Формат ввода:
Вводится строка.


Формат вывода:
Выведите ответ на задачу.


Примеры:
Тест 1
>>> Bilbo.Baggins@bagend.hobbiton.shire.me
Bilbo.Bagginsbagend.hobbiton.shire.me

Тест 2
>>> dfa;sdkfj;ajva;bvna'sdasdfasdglJLHJKFHLDKJFh
dfa;sdkfj;ajva;bvna'sdasdfasdglJLHJKFHLDKJFh

Тест 3
>>> @

"""

s = input()
s = s.replace('@', '')
print(s)
