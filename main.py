import sys, getopt
from classes.filehelper import FileReader

PHP_LANG = 'PHP'


def main(argv):
    directory = ''
    lang = PHP_LANG
    file = 'app'

    try:
        opts, args = getopt.getopt(argv, "dlf:", ["dir=", "lang=", "file="])
    except getopt.GetoptError:
        print('Unrecognized params')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-d", "--dir"):
            directory = arg
        if opt in ("-l", "--lang"):
            lang = arg
        if opt in ("-f", "--file"):
            file = arg

    fr = FileReader(directory, lang)
    translations = fr.get_translations()

    if lang == PHP_LANG:
        fr.array_as_php(translations)
    else:
        print(translations)

    exit(0)


if __name__ == "__main__":
    main(sys.argv[1:])