import os
import shutil


def catalogizator(path):
    # Открываем директорию и считываем все файлы
    for file in os.listdir(rf'{path}'):
        # Создаем полный путь до файла
        file_path = os.path.join(path, file)

        # Проверяем, является ли объект файлом, а не директорией
        if os.path.isfile(file_path):
            # Если объект - файл, то отделяем расширение от файла
            name, extension = os.path.splitext(file)
            # создаем новый путь до директории с названием расширения
            new_dir = os.path.join(path, extension[1::])
            # и если такой диреткории не существует, создаем ее
            if not os.path.exists(new_dir):
                os.mkdir(new_dir)

            # После чего переносим все файлы в созданные директории
            new_path_file = os.path.join(new_dir, file)
            shutil.move(file_path, new_path_file)


path = input('Введите путь к директории:')
while not os.path.exists(path):
    print('Ошибка нахождения пути. Данная директория отсутствует в системе')
    path = input('Введите путь к директории:')

catalogizator(path)

print('Каталоги успешно созданы. Файлы перемещены.')
