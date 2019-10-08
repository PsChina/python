#coding=utf-8

def main():
    f = open('README.md', 'r', encoding='utf-8')
    print(f.read())
    f.close()


if __name__ == '__main__':
    main()