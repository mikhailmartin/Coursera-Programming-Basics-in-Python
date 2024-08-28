"""
Продажи

Дана база данных о продажах некоторого интернет-магазина. Каждая строка
входного файла представляет собой запись вида

Покупатель товар количество, где

Покупатель — имя покупателя (строка без пробелов),

товар — название товара (строка без пробелов),

количество — количество приобретенных единиц товара.

Создайте список всех покупателей, а для каждого покупателя подсчитайте
количество приобретенных им единиц каждого вида товаров.


Формат ввода:
Вводятся сведения о покупках в указанном формате.


Формат вывода:
Выведите список всех покупателей в лексикографическом порядке, после имени
каждого покупателя выведите двоеточие, затем выведите список названий всех
приобретенных данным покупателем товаров в лексикографическом порядке, после
названия каждого товара выведите количество единиц товара, приобретенных данным
покупателем. Информация о каждом товаре выводится в отдельной строке.


Примеры:
Тест 1
input: Ivanov paper 10
input: Petrov pens 5
input: Ivanov marker 3
input: Ivanov paper 7
input: Petrov envelope 20
input: Ivanov envelope 5
output: Ivanov:
output: envelope 5
output: marker 3
output: paper 17
output: Petrov:
output: envelope 20
output: pens 5

Тест 2
input: Ivanov aaa 1
input: Petrov aaa 2
input: Sidorov aaa 3
input: Ivanov aaa 6
input: Petrov aaa 7
input: Sidorov aaa 8
input: Ivanov bbb 3
input: Petrov bbb 7
input: Sidorov aaa 345
input: Ivanov ccc 45
input: Petrov ddd 34
input: Ziborov eee 234
input: Ivanov aaa 45
input: Ivanov aaa 45
output: Ivanov:
output: aaa 52
output: bbb 3
output: ccc 45
output: Petrov:
output: aaa 9
output: bbb 7
output: ddd 34
output: Sidorov:
output: aaa 356
output: Ziborov:
output: eee 234

Тест 3
input: TKSNUU FKXYPUGQ 855146
input: TKSNUU FKXYPUGQ 930060
input: TKSNUU FKXYPUGQ 886973
input: TKSNUU FKXYPUGQ 59344
input: TKSNUU FKXYPUGQ 296343
input: TKSNUU FKXYPUGQ 193166
input: TKSNUU FKXYPUGQ 211696
input: TKSNUU FKXYPUGQ 821064
input: TKSNUU FKXYPUGQ 672846
input: TKSNUU FKXYPUGQ 820341
input: TKSNUU FKXYPUGQ 350693
input: TKSNUU FKXYPUGQ 469538
input: TKSNUU FKXYPUGQ 849069
input: TKSNUU FKXYPUGQ 502007
input: TKSNUU FKXYPUGQ 961595
input: TKSNUU FKXYPUGQ 747271
input: TKSNUU FKXYPUGQ 863648
input: TKSNUU FKXYPUGQ 952069
input: TKSNUU FKXYPUGQ 286019
input: TKSNUU FKXYPUGQ 364841
input: TKSNUU FKXYPUGQ 455930
input: TKSNUU FKXYPUGQ 100486
input: TKSNUU FKXYPUGQ 335026
input: TKSNUU FKXYPUGQ 197672
input: TKSNUU FKXYPUGQ 217640
input: TKSNUU FKXYPUGQ 612549
input: TKSNUU FKXYPUGQ 622501
input: TKSNUU FKXYPUGQ 96554
input: TKSNUU FKXYPUGQ 327166
input: TKSNUU FKXYPUGQ 425399
input: TKSNUU FKXYPUGQ 362309
input: TKSNUU FKXYPUGQ 78477
input: TKSNUU FKXYPUGQ 258916
input: TKSNUU FKXYPUGQ 297923
input: TKSNUU FKXYPUGQ 8891
input: TKSNUU FKXYPUGQ 13639
input: TKSNUU FKXYPUGQ 77308
input: TKSNUU FKXYPUGQ 707620
input: TKSNUU FKXYPUGQ 68205
input: TKSNUU FKXYPUGQ 256702
input: TKSNUU FKXYPUGQ 668334
input: TKSNUU FKXYPUGQ 968673
input: TKSNUU FKXYPUGQ 138125
input: TKSNUU FKXYPUGQ 222904
input: TKSNUU FKXYPUGQ 214091
input: TKSNUU FKXYPUGQ 500231
input: TKSNUU FKXYPUGQ 19611
input: TKSNUU FKXYPUGQ 491343
input: TKSNUU FKXYPUGQ 404307
input: TKSNUU FKXYPUGQ 68367
input: TKSNUU FKXYPUGQ 287107
input: TKSNUU FKXYPUGQ 794935
input: TKSNUU FKXYPUGQ 254217
input: TKSNUU FKXYPUGQ 206370
input: TKSNUU FKXYPUGQ 202761
input: TKSNUU FKXYPUGQ 929017
input: TKSNUU FKXYPUGQ 843359
input: TKSNUU FKXYPUGQ 955269
input: TKSNUU FKXYPUGQ 134139
input: TKSNUU FKXYPUGQ 946168
input: TKSNUU FKXYPUGQ 967781
input: TKSNUU FKXYPUGQ 856474
input: TKSNUU FKXYPUGQ 465070
input: TKSNUU FKXYPUGQ 580526
input: TKSNUU FKXYPUGQ 172109
input: TKSNUU FKXYPUGQ 191703
input: TKSNUU FKXYPUGQ 207916
input: TKSNUU FKXYPUGQ 512264
input: TKSNUU FKXYPUGQ 533081
input: TKSNUU FKXYPUGQ 577208
input: TKSNUU FKXYPUGQ 831389
input: TKSNUU FKXYPUGQ 439158
input: TKSNUU FKXYPUGQ 565633
input: TKSNUU FKXYPUGQ 452643
input: TKSNUU FKXYPUGQ 164426
input: TKSNUU FKXYPUGQ 540743
input: TKSNUU FKXYPUGQ 880704
input: TKSNUU FKXYPUGQ 868529
input: TKSNUU FKXYPUGQ 240742
input: TKSNUU FKXYPUGQ 868865
input: TKSNUU FKXYPUGQ 910442
input: TKSNUU FKXYPUGQ 146737
input: TKSNUU FKXYPUGQ 820984
input: TKSNUU FKXYPUGQ 660948
input: TKSNUU FKXYPUGQ 957975
input: TKSNUU FKXYPUGQ 135847
input: TKSNUU FKXYPUGQ 401865
input: TKSNUU FKXYPUGQ 982859
input: TKSNUU FKXYPUGQ 748454
input: TKSNUU FKXYPUGQ 354734
input: TKSNUU FKXYPUGQ 525638
input: TKSNUU FKXYPUGQ 119140
input: TKSNUU FKXYPUGQ 484816
input: TKSNUU FKXYPUGQ 616539
input: TKSNUU FKXYPUGQ 682553
input: TKSNUU FKXYPUGQ 841541
input: TKSNUU FKXYPUGQ 713063
input: TKSNUU FKXYPUGQ 433453
input: TKSNUU FKXYPUGQ 465340
input: TKSNUU FKXYPUGQ 985635
output: TKSNUU:
output: FKXYPUGQ 49769497
"""
INPUT_FILE_NAME = "input.txt"


input_file = open(INPUT_FILE_NAME, "r", encoding="utf8")

customers = dict()
for line in input_file:
    customer, product, number = line.split()
    customers[customer] = customers.get(customer, dict())
    customers[customer][product] = customers[customer].get(product, 0) + int(number)

for customer in sorted(customers):
    print(customer, ":", sep="")
    for product in sorted(customers[customer]):
        print(product, customers[customer][product])
