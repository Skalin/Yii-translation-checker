import sys, getopt
from sample.filehelper import FileReader



def main(argv):
    dir = ''
    try:
        opts, args = getopt.getopt(argv, "d:", ["dir="])
    except getopt.GetoptError:
        print('Unrecognized params')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-d", "--dir"):
            dir = arg

    fr = FileReader(dir)
    files = fr.getFiles(fr.dir)
    translations = fr.getTranslations(files)

    fr.arrayAsPhp(translations)
    exit(0)





if __name__ == "__main__":
    main(sys.argv[1:])