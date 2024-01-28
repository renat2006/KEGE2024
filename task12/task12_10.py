"""
НАЧАЛО
ПОКА нашлось (31)
    заменить (31, 7)
КОНЕЦ ПОКА
КОНЕЦ
Исходная строка содержит две девятки, двенадцать единиц и некоторое
количество троек, других цифр нет, точный порядок расположения единиц,
троек и девяток неизвестен. После выполнения программы получилась строка с суммой цифр 60.
Какое наименьшее количество троек могло быть в исходной строке?
"""
k = 0
maxx = 1
for n in range(1, int(1e4)):
    s = "31" * n + "1" * (12 - n) + "9" * 2

    while "31" in s:
        s = s.replace("31", "7", 1)

    sum_of_s = sum(map(int, s))
    if sum_of_s == 60:
        print(n)
        break