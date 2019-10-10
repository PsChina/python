#coding=utf-8

def main():
    f = open('README.md', 'r', encoding='utf-8')
    print(f.read())
    f.close()

def print_text_line_by_line():
    f = open('README.md', 'r', encoding='utf-8')
    line_index = 1
    for each_line in f:
        print("%d:%s" % (line_index, each_line))
        line_index += 1

def write_file():
        open('a.js','w', encoding='utf-8').write(str('const a = 10; console.log(a)'))

if __name__ == '__main__':
    # main()
    # print_text_line_by_line()
    write_file()