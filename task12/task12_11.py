"""
Цикл

    ПОКА условие
        последовательность команд
    КОНЕЦ ПОКА
выполняется, пока условие истинно. В конструкции

    ЕСЛИ условие
        ТО команда1
        ИНАЧЕ команда2
    КОНЕЦ ЕСЛИ
выполняется команда1 (если условие истинно) или команда2 (если условие ложно).
Дана программа для Редактора:

НАЧАЛО
ПОКА нашлось (01) ИЛИ нашлось (02) ИЛИ нашлось (03)
    заменить (01, 20)
    заменить (02, 301)
    заменить (03, 1102)
КОНЕЦ ПОКА
КОНЕЦ
Известно, что исходная строка начиналась с нуля, а далее содержала только единицы,
двойки и тройки. После выполнения данной программы получилась строка, содержащая 20 единиц, 100 двоек и 40 троек.
Сколько единиц было в исходной строке?
"""
k = 0
maxx = 1
for x in range(int(70)):
    for y in range(int(70)):
        for z in range(int(70)):

            s = "0" + "1" * x + "2" * y + "3" * z
            s1 = s

            while "01" in s or "02" in s or "03" in s:
                s = s.replace("01", "20", 1)
                s = s.replace("02", "301", 1)
                s = s.replace("03", "1102", 1)

            if s.count("1") == 20 and s.count("2") == 100 and s.count("3") == 40:
                print(s1.count("1"))
                break