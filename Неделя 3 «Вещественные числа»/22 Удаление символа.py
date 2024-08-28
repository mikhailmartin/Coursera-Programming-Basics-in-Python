"""
Удаление символа

Дана строка. Удалите из этой строки все символы @.


Формат ввода:
Вводится строка.


Формат вывода:
Выведите ответ на задачу.


Примеры:
Тест 1
input: Bilbo.Baggins@bagend.hobbiton.shire.me
output: Bilbo.Bagginsbagend.hobbiton.shire.me

Тест 2
input: dfa;sdkfj;ajva;bvna'sdasdfasdglJLHJKFHLDKJFh
output: dfa;sdkfj;ajva;bvna'sdasdfasdglJLHJKFHLDKJFh

Тест 3
input: @
output:
"""
s = input()

s = s.replace('@', '')
print(s)
