"""
Банковские счета

Некоторый банк хочет внедрить систему управления счетами клиентов,
поддерживающую следующие операции:

Пополнение счёта клиента.

Снятие денег со счёта.

Запрос остатка средств на счёте.

Перевод денег между счетами клиентов.

Начисление процентов всем клиентам.

Вам необходимо реализовать такую систему. Клиенты банка идентифицируются
именами (уникальная строка, не содержащая пробелов). Первоначально у банка нет
ни одного клиента. Как только для клиента проводится операция пополнения,
снятия или перевода денег, ему заводится счёт с нулевым балансом. Все
дальнейшие операции проводятся только с этим счётом. Сумма на счету может быть
как положительной, так и отрицательной, при этом всегда является целым числом.


Формат ввода:
Входной файл содержит последовательность операций. Возможны следующие операции:

DEPOSIT name sum - зачислить сумму sum на счёт клиента name. Если у клиента нет
счёта, то счёт создаётся.

WITHDRAW name sum - снять сумму sum со счёта клиента name. Если у клиента нет
счёта, то счёт создаётся.

BALANCE name - узнать остаток средств на счету клиента name.

TRANSFER name1 name2 sum - перевести сумму sum со счёта клиента name1 на счёт
клиента name2. Если у какого-либо клиента нет счета, то ему создается счёт.

INCOME p - начислить всем клиентам, у которых открыты счета, p% от суммы счёта.
Проценты начисляются только клиентам с положительным остатком на счету, если у
клиента остаток отрицательный, то его счёт не меняется. После начисления
процентов сумма на счету остаётся целой, то есть начисляется только целое число
денежных единиц. Дробная часть начисленных процентов отбрасывается.


Формат вывода:
Для каждого запроса BALANCE программа должна вывести остаток на счету данного
клиента. Если же у клиента с запрашиваемым именем не открыт счёт в банке,
выведите ERROR.


Примеры:
Тест 1
input: DEPOSIT Ivanov 100
input: INCOME 5
input: BALANCE Ivanov
input: TRANSFER Ivanov Petrov 50
input: WITHDRAW Petrov 100
input: BALANCE Petrov
input: BALANCE Sidorov
output: 105
output: -50
output: ERROR

Тест 2
input: BALANCE Ivanov
input: BALANCE Petrov
input: DEPOSIT Ivanov 100
input: BALANCE Ivanov
input: BALANCE Petrov
input: DEPOSIT Petrov 150
input: BALANCE Petrov
input: DEPOSIT Ivanov 10
input: DEPOSIT Petrov 15
input: BALANCE Ivanov
input: BALANCE Petrov
input: DEPOSIT Ivanov 46
input: BALANCE Ivanov
input: BALANCE Petrov
input: DEPOSIT Petrov 14
input: BALANCE Ivanov
input: BALANCE Petrov
output: ERROR
output: ERROR
output: 100
output: ERROR
output: 150
output: 110
output: 165
output: 156
output: 165
output: 156
output: 179

Тест 3
input: BALANCE a
input: BALANCE b
input: DEPOSIT a 100
input: BALANCE a
input: BALANCE b
input: WITHDRAW a 20
input: BALANCE a
input: BALANCE b
input: WITHDRAW b 78
input: BALANCE a
input: BALANCE b
input: WITHDRAW a 784
input: BALANCE a
input: BALANCE b
input: DEPOSIT b 849
input: BALANCE a
input: BALANCE b
output: ERROR
output: ERROR
output: 100
output: ERROR
output: 80
output: ERROR
output: 80
output: -78
output: -704
output: -78
output: -704
output: 771
"""
INPUT_FILE_NAME = "input.txt"


input_file = open(INPUT_FILE_NAME, "r", encoding="utf8")

accounts = dict()
for line in input_file:
    line = line.split()
    if line[0] == "DEPOSIT":
        name = line[-2]
        summ = int(line[-1])

        accounts[name] = accounts.get(name, 0) + summ
    elif line[0] == "WITHDRAW":
        name = line[-2]
        summ = int(line[-1])

        accounts[name] = accounts.get(name, 0) - summ
    elif line[0] == "BALANCE":
        name = line[-1]

        print(accounts.get(name, "ERROR"))
    elif line[0] == "TRANSFER":
        name1 = line[-3]
        name2 = line[-2]
        summ = int(line[-1])

        accounts[name1] = accounts.get(name1, 0) - summ
        accounts[name2] = accounts.get(name2, 0) + summ
    elif line[0] == "INCOME":
        p = int(line[-1])

        for name in accounts:
            if accounts[name] > 0:
                accounts[name] += int(accounts[name] * (p / 100))
