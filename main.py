import sys, getopt
from classes.filehelper import FileReader


def main(argv):
    directory = ''
    try:
        opts, args = getopt.getopt(argv, "d:", ["dir="])
    except getopt.GetoptError:
        print('Unrecognized params')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-d", "--dir"):
            directory = arg

    fr = FileReader(directory)
    files = fr.get_files(fr.dir)
    translations = fr.get_translations(files)

    fr.array_as_php(translations)
    exit(0)


if __name__ == "__main__":
    main(sys.argv[1:])