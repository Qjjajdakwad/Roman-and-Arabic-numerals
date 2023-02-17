#module (Library)
roman_table = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]


def roman_to_int(i):
    Arab = 0
    for int, rome in roman_table:
        while i.startswith(rome):
            Arab += int
            i = i[len(rome):]
    return Arab


def int_to_roman(i):
    global  roman_table
    roman_number = ""

    while i>0:
        for int, rome in roman_table:
            while i >= int:
                roman_number += rome
                i -= int
    return roman_number

