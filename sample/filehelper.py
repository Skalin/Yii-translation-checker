import os
import re

translation_string = 'Yii::t(\'app\', \''


class FileReader:

    files = []

    def __init__(self, dir):
        self.dir = dir


    def getFiles(self, dir):
        for filename in os.listdir(dir):
            fn = dir+'/'+filename
            if os.path.isdir(fn):
                self.getFiles(fn)

            if os.path.isfile(fn):
                if fn.endswith('.php'):
                    self.files.append(fn)

        return self.files

    def getTranslations(self, files):
        translations = []
        for file in files:
            with open(file, 'r') as content_file:
                content = content_file.read()
                starts = [match.start() for match in re.finditer(re.escape(translation_string), content)]
                if len(starts) != 0:
                    for start in starts:
                        end = content.find('\'', start+len(translation_string))
                        translations.append(content[start+len(translation_string):end])

        return translations

    def arrayAsPhp(self, array):
        for item in array:
            print(item+' => '+item)
