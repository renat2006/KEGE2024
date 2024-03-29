"""
НАЧАЛО
ПОКА нашлось (>1) ИЛИ нашлось (>2) ИЛИ нашлось (>3)
    ЕСЛИ нашлось (>1)
        ТО заменить (>1, 23>)
    КОНЕЦ ЕСЛИ
    ЕСЛИ нашлось (>2)
        ТО заменить (>2, 21>)
    КОНЕЦ ЕСЛИ
    ЕСЛИ нашлось (>3)
        ТО заменить (>3, 7>)
    КОНЕЦ ЕСЛИ
КОНЕЦ ПОКА
КОНЕЦ
На вход приведённой выше программе поступает строка, начинающаяся с символа «>», а затем содержащая 14 цифр «1», 11 цифр «2» и n цифр «3», расположенных в произвольном порядке.
Определите наименьшее положительное значение n, при котором сумма числовых значений цифр строки, получившейся в результате выполнения программы, является простым числом.
В ответ запишите найденное n, а затем соответствующее простое число без пробелов, запятых и других разделителей.
"""


class SuperInt:
    def __init__(self, n):
        self.n = int(n)

    def get_dividers(self):
        a = self.n
        devs = {1, a}
        d = 2

        while a > 0 and d * d <= a:
            if a % d == 0:
                devs.add(d)
                devs.add(a // d)
            d += 1

        return devs

    def __str__(self):
        return str(self.n)


for n in range(1, int(1e5)):
    s = ">" + "1" * 14 + "2" * 11 + "3" * n

    while ">1" in s or ">2" in s or ">3" in s:
        s = s.replace(">1", "23>", 1)

        s = s.replace(">2", "21>", 1)
        s = s.replace(">3", "7>", 1)
    sum_of_s = sum(map(int, s.replace(">", "")))
    if len(SuperInt(sum_of_s).get_dividers()) == 2:
        print(n, sum_of_s, sep="")
        break
