"""
НАЧАЛО
ПОКА нашлось (@$) ИЛИ нашлось (\@) ИЛИ нашлось (\$)
    ЕСЛИ нашлось (@$)
        ТО заменить (@$, $@)
    КОНЕЦ ЕСЛИ
    ЕСЛИ нашлось (\@)
        ТО заменить (\@, @\)
    КОНЕЦ ЕСЛИ
    ЕСЛИ нашлось (\$)
        ТО заменить (\$, $\)
    КОНЕЦ ЕСЛИ
КОНЕЦ ПОКА
КОНЕЦ
На вход редактору подаётся строка, содержащая равное количество символов @, $ и \, расположенных в произвольном порядке.
При каком максимальном количестве символов в исходной строке в преобразованной строке на позиции под номером 30 будет стоять символ @?
Позиции в строке нумеруются с единицы слева направо.
"""

k = 0
maxx = 30

for x in range(100):

    s = "\\" * x + "@" * x + "$" * x

    while "@$" in s or "\@" in s or "\$" in s:
        s = s.replace("@$", "$@", 1)

        s = s.replace("\@", "@\\", 1)

        s = s.replace("\$", "$\\", 1)
    if x * 3 > maxx and s[29] == "@":
        maxx = x * 3
print(maxx)
