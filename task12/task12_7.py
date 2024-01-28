"""
НАЧАЛО
ПОКА нашлось (000) ИЛИ нашлось (40) ИЛИ нашлось (100)
    ЕСЛИ нашлось (000)
        ТО заменить (000, 1)
    КОНЕЦ ЕСЛИ
    ЕСЛИ нашлось (40)
        ТО заменить (40, 0)
    КОНЕЦ ЕСЛИ
    ЕСЛИ нашлось (100)
        ТО заменить (100, 04)
    КОНЕЦ ЕСЛИ
КОНЕЦ ПОКА
КОНЕЦ
На вход приведённой выше программе поступает строка, начинающаяся на "4" и содержащая n цифр "0" (3 < n < 10000).
Определите наибольшее возможное значение суммы числовых значений цифр строки, которая может быть результатом выполнения программы.
Примечание. Вероятно, программа не мгновенно выдаст ответ. Придётся подождать 15+ секунд. Но эта задача создана на основе задачи из реального варианта ЕГЭ-23, где экзаменуемые столкнулись с той же проблемой.
"""
k = 0
maxx = 1
for n in range(3, int(1e4)):
    s = "4" + "0" * n

    while "000" in s or "40" in s or "100" in s:
        s = s.replace("000", "1", 1)

        s = s.replace("40", "0", 1)
        s = s.replace("100", "04", 1)
    sum_of_s = sum(map(int, s))
    if sum_of_s > maxx:
        maxx = sum_of_s
print(maxx)