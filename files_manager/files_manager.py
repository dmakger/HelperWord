import os
from os import listdir
from os.path import isfile, join


class FilesManager:
    dir_name = 'docs'

    def getFilesInDir(self, dir_name=dir_name):
        # if file.endswith('docx') and not file.startswith('~'):
        paths = []

        # dir_name = os.getcwd()
        for root, dirs, files in os.walk(dir_name):
            # file = isfile(join(dir_name, f))
            for file in files:
                if (file.endswith('docx') or file.endswith('doc')) and not file.startswith('~'):
                    paths.append(os.path.join(root, file))
                    # paths.append(os.path.abspath(os.path.join(root, file)))
        return paths
        #     if file.endswith('docx') and not file.startswith('~'):
        # return [os.path.abspath(f) for f in listdir(dir_name) if isfile(join(dir_name, f))]
        # return [f"{dir_name}\\{f}" for f in listdir(dir_name) if isfile(join(dir_name, f))]
