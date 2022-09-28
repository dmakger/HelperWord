from files_manager.files_manager import FilesManager
from word.word_file_manager import WordFileManager


if __name__ == '__main__':
    dir_name = '2022'
    files = FilesManager().getFilesInDir()
    print(files)
    for f in files:
        file = f.split('\\')[1]
        file_name, file_res = file.split('.')
        new_file = f"{dir_name}\\{file_name}.{file_res}"
        print(new_file)

        file_manager = WordFileManager(f)
        file_manager.replace_text('2021', '2022')
        #
        file_manager.save(new_file)
