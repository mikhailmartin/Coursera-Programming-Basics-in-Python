"""
Словарь синонимов

Вам дан словарь, состоящий из пар слов. Каждое слово является синонимом к
парному ему слову. Все слова в словаре различны. Для одного данного слова
определите его синоним.


Формат ввода:
Программа получает на вход количество пар синонимов N. Далее следует N строк,
каждая строка содержит ровно два слова-синонима. После этого следует одно
слово.


Формат вывода:
Программа должна вывести синоним к данному слову.


Примечания:
Эту задачу можно решить и без словарей (сохранив все входные данные в списке),
но решение со словарем будет более простым.


Примеры:
Тест 1
input: 3
input: Hello Hi
input: Bye Goodbye
input: List Array
input: Goodbye
output: Bye

Тест 2
input: 1
input: beep Car
input: Car
output: beep

Тест 3
input: 2
input: Ololo Ololo
input: Numbers 1234567890
input: Numbers
output: 1234567890
"""
n = int(input())

synonyms = dict()
for _ in range(n):
    word1, word2 = input().split()
    synonyms[word1] = word2
    synonyms[word2] = word1

word = input().strip()
print(synonyms[word])
