"""
Учительница задала Пете домашнее задание — в заданном тексте расставить
ударения в словах, после чего поручила Васе проверить это домашнее задание.
Вася очень плохо знаком с данной темой, поэтому он нашёл словарь, в котором
указано, как ставятся ударения в словах. К сожалению, в этом словаре
присутствуют не все слова. Вася решил, что в словах, которых нет в словаре, он
будет считать, что Петя поставил ударения правильно, если в этом слове Петей
поставлено ровно одно ударение.

Оказалось, что в некоторых словах ударение может быть поставлено больше, чем
одним способом. Вася решил, что в этом случае если то, как Петя поставил
ударение, соответствует одному из приведённых в словаре вариантов, он будет
засчитывать это как правильную расстановку ударения, а если не соответствует,
то как ошибку. Вам дан словарь, которым пользовался Вася и домашнее задание,
сданное Петей. Ваша задача — определить количество ошибок, которое в этом
задании насчитает Вася.


Формат ввода:
Вводится сначала число N — количество слов в словаре (0 ≤ N ≤ 20000). Далее
идёт N строк со словами из словаря. Каждое слово состоит не более чем из 30
символов. Все слова состоят из маленьких и заглавных латинских букв. В каждом
слове заглавная ровно одна буква — та, на которую попадает ударение. Слова в
словаре расположены в алфавитном порядке. Если есть несколько возможностей
расстановки ударения в одном и том же слове, то эти варианты в словаре идут в
произвольном порядке.

Далее идёт упражнение, выполненное Петей. Упражнение представляет собой строку
текста, суммарным объёмом не более 300000 символов. Строка состоит из слов,
которые разделяются между собой ровно одним пробелом. Длина каждого слова не
превышает 30 символов. Все слова состоят из маленьких и заглавных латинских
букв (заглавными обозначены те буквы, над которыми Петя поставил ударение).
Петя мог по ошибке в каком-то слове поставить более одного ударения или не
поставить ударения вовсе.


Формат вывода:
Выведите количество ошибок в Петином тексте, которые найдёт Вася.


Примечания:
Примечания к примерам тестов

1. В слове cannot, согласно словарю возможно два варианта расстановки ударения.
Эти варианты в словаре могут быть перечислены в любом порядке (т.е. как сначала
cAnnot, а потом cannOt, так и наоборот). Две ошибки, совершенные Петей — это
слова be (ударение вообще не поставлено) и fouNd (ударение поставлено неверно).
Слово thE отсутствует в словаре, но поскольку в нём Петя поставил ровно одно
ударение, признаётся верным.

2. Неверно расставлены ударения во всех словах, кроме The (оно отсутствует в
словаре, в нём поставлено ровно одно ударение). В остальных словах либо ударные
все буквы (в слове PAGE), либо не поставлено ни одного ударения.


Примеры:
Тест 1
>>> 4
>>> cAnnot
>>> cannOt
>>> fOund
>>> pAge
>>> thE pAge cAnnot be fouNd
2

Тест 2
>>> 4
>>> cAnnot
>>> cannOt
>>> fOund
>>> pAge
>>> The PAGE cannot be found
4

Тест 3
>>> 0
>>> ciFqrfIxe LgvqquN zvdlhnXJ tizFPXtv JxqWqgnR CabaJ hFYoqbhH UyfiTXO
YvAylvnc ymtHHfnqh bmTLsEnh hikroekt dtVSftFBz ofQrMfo jGTGofv dVRwfJw UaRfzE
wbjjGsM xKcezhleq XskqyXtl pWCkyr JcuiiawHw hHBbOV pIfztqkuo PNbjXhtoi lvthZdUc
oozdiZCq xDdnpRqsD HDfocjpl aziTbCh jsJMkTpaG voKfnjYb ADtpndbo gwOkCvJs
hGnvtbM NkFodqOwy BOgxWv qzMsbelpO tlQnic QlxjhTzNj OZvzmoNX NlbLsjq OvkpysLzc
BFCjEESh aiLyKJas zhJbcdu vqxrKhgke BsEikapC aCCoHAFR qNSYNouc TboUQd bOJWCAy
NiNkHPmA wsGXhub xIvDhv qeGgpTBkd XPOkfsxz bbgcyuWq YHioAxh mngcZbpgh qgbfVztk
JMusos ogpskgdN HUmedvmA GhhpYKH vduijcpv rfMZlB rvpodvq UogggJX yhnKvOpz
cKQHazal xdXpPMCzn zaYdrbic FYDsrfaF kFpUcXtY jihQVZ nhpgJXoT rwJokNFH eGvoNulk
LugdwQRbl xlRQdy mOrvmCmhG tJpEDolo zLhXCegyl Orrnefa sQqsjckkm BaadhPSXa
vLmbthY mlwXEbpns oLctMjmM spQHUtA qnxUrLGo ScAndtRh apdwiTV odtrlufr zkrreoWHT
wbOJLyIvn TDPtdjFp CJtnhbNr ohkLVpww vJLdOfp ctswuolD kuIdtiWLq pHQvvlN
uzEgrQhpG ncHyqZzt gkntqtmx ZAvUjYgJ hbjSXnN URnTcdbRk wMdRlrQ ilpvgMpja
oIjXxmG sdnIJTkk bFvhViK dpdtgpt CembyhyMM RcBIirR rWyYzJfc UNbTfQQ plxhCpee
bUbkgdDF JTgQAQhvp onFayvlm rykjyldhw xAuEnxF phbhlXB xxDDxfSfM aPHXcXsag
sTseOhrrY MMiaCH avfBbeIfl hrtuxe zJlubLs Wwwdjvc JBnqWcAl hDXOdeHZr Nelvhp
ydmbzqym kzbCxuN rNQCDbeqB VRaax yykZbEzOc XomeWckS jBrCrHrx FzGrd YvfUzRryb
YYPSRO wxBazrm EkezBXg aUiYcod aTtjEEpz WczSYbDx tlFeIKB LlSQDtyVa iMGfoQ WyXVU
wakvcqSU loKOoSnzA pWywmptia RcEMjACB bfyrkwpLp iSofdn SacAoja uIkcgpWnM
dkqErpG nkxTwHfh srejafR rjXxUCQ BCstjy LBdeArjn SbunWWcd FmTkfGwh nyGRjOi
VlZjliwD lQhjguWx IkemfP VGfqFBuiN aYrbvKu iabtpq QnjzcKE sffhhZYY JuooLppkr
LqyjiBC WySPUmsQb CXjftV TmtgreN cicNuaor YIgdgc vTFwiGktI TNFmWdHU DpfEtwtf
zssykzEsf xcsCKfnaS OBEwUVkzg PgArpsz RmUcaQels JmJaqn IcXnrvhkg vgkOPzmv
BezbGaMfb bnjTmLse TnkNLq CxfpAoD slhLtnoaP jnppioo STcoufpS XmRtQqd yDpbsld
qrVIEXn VZhmozgvr zuELbtea WiOopcPg vRwLRoy TyJkPUvOq yZSsjoi AzlwLPf suwNmPrzF
kuJeUivG EnTHwlj XpZkNZH xygjBcx bTytkWFW ygKis iwjgktgw DzFDkhb elWPfddxy
TyvlSNVR OBqjNCtXI cSYxJTb DqedLuqN vxikfztEc AbcQgnxiS bdCmDnn VbLDUWsz
eeuucmp osIYklu sLXmxRipG yswHjZayD bMihpnRs lmyVpf gtfkgpmbB buPjpqli yxFSIu
Ggjzeqm dTqrvPtei XduXypxn BykKgHhqe ewcUDvM lxWoiXBT HeqhAZu ialinsqW lcNzJmK
yCKPbQrz hOjxGWvPq HgenCiuw QnWaEtz lRvwixAj otnJuciJ qtNWZPtL tJYiHzUiG
rNhaIjil Oggvgmdq nhylWth VhrHlcnJV ceHFAVnU udtpWoJ wiQAeN mUkmTUv BqnLMdeSy
kiffoynx vsnzxZe QbyfijgM ecxxWebWo TFoLnXouN SldaeWjV fuXlPWzBg qNNShyw
avvNUgmP lhblkew svZdutKT avlFkl Afntea NrGVToH Hlvkxnut NbNbQXnc ugqqBFWcq
bphIBvYpz FuuAUB CnqFfWxy lNdVncXmk UBvozFuqz muVHqMpa vcyQgcXN lfzcMdN eMmz
ehXopYXAg GjBapgXVY qimorSZZt YEyoXzclm eUlyvxi aFrOSW htxGkVuJ ydszmKyb
zAvzlkXM oRQizsGBz gZodlbKg pwQSugvyq MOvfpsCs tGNJBf lZqEdtPD sHYmFjcH
wkRltsoYz qkWmhhBJ wgATDnhc HnbkMwnRv oSolCjBj xyQfzgenj xBtaqrEj eoCCfSg
xYgfXZ htSgaFlbt DPrfLUw bdhrUaqT IabsomJE cyVtEg SMntmDjx jwwkwJkRo HeFyGSaTh
KiSTzh dBCcqt vnAunEzf kGzwbur qmkMBbGCw Tdkunrkh YrYVnrbC muJSHjn Unuwgjfj
ObbZfLsWd UjmxpJN KNlbLhF jFlbrLf pyOglEK
296
"""

INPUT_FILE_NAME = 'input.txt'


def main():
    input_file = open(INPUT_FILE_NAME, 'r', encoding='utf8')

    n = int(input_file.readline())

    dictionary = dict()
    for _ in range(n):
        accent = input_file.readline().strip()
        word = accent.lower()
        if word not in dictionary:
            dictionary[word] = [accent]
        else:
            dictionary[word].append(accent)

    def upper_count(string):
        count = 0
        for char in accent:
            if char.isupper():
                count += 1
        return count

    error_count = 0
    test = input_file.readline().split()
    for accent in test:
        word = accent.lower()
        if word in dictionary:
            if accent not in dictionary[word]:
                error_count += 1
        else:
            if upper_count(accent) != 1:
                error_count += 1

    print(error_count)


main()
