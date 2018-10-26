import os
import re
from classes.common import Common


class FileReader:

    files = []
    translation_string = ''

    def __init__(self, directory, file=None):
        self.directory = directory
        if file is not None:
            self.file = file
            self.translation_string = 'Yii::t(\''+self.file+'\', \''
        else:
            self.translation_string = 'Yii::t(\'app\', \''

    def get_files(self, directory=None):
        if directory is None:
            directory = self.directory
        if len(os.listdir(directory)) == 0:
            Common.exception(2, 'Directory is empty')
        for filename in os.listdir(directory):
            fn = directory+'/'+filename
            if os.path.isdir(fn):
                self.get_files(fn)

            if os.path.isfile(fn):
                if fn.endswith('.php'):
                    self.files.append(fn)

        return self.files

    def get_translations(self, files=None):
        translations = []
        if files is None:
            files = self.get_files()
        for file in files:
            with open(file, 'r', encoding='utf8') as content_file:
                content = content_file.read()
                starts = [match.start() for match in re.finditer(re.escape(self.translation_string), content)]
                if len(starts) != 0:
                    for start in starts:
                        end = content.find('\'', start+len(self.translation_string))
                        translations.append(content[start+len(self.translation_string):end])

        return translations

    @staticmethod
    def array_as_php(array):
        for item in array:
            print('\''+item+'\''+' => '+'\''+item+'\'')
