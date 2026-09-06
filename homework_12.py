
def line_exchange():
    text = 'Замена строки в текстовом файле; \nзаписать список в файл;\nизменить строку в списке;\n'
    with open(file, 'w', encoding='utf-8') as f:
        f.write(text)


def text2():
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        pos1 = int(input('pos1 = '))
        pos2 = int(input('pos2 = '))
        lines[pos1], lines[pos2] = lines[pos2], lines[pos1]
        print(lines)
        return lines


def write_text(lines):
    with open(file, 'w', encoding='utf-8') as f:
        f.writelines(lines)


file = 'text1.txt'
line_exchange()
a = text2()
write_text(a)