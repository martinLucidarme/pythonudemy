import os
from PIL import Image


def main(main_images_folder, new_width=800):
    if not os.path.isdir(main_images_folder):
        raise NotADirectoryError
    for root, dirs, files in os.walk(main_images_folder):
        for file in files:
            file_full_path = os.path.join(root, file)
            file_name, extension = os.path.splitext(file)

            converted_tag = '_converted'

            new_file = file_name + converted_tag + extension
            new_file_full_path = os.path.join(root, new_file)

            if converted_tag in file_full_path:  # imagem ja convertida
                #  os.remove(file_full_path)  # para apagar as imagens geradas
                continue

            img_pillow = Image.open(file_full_path)
            width, height = img_pillow.size
            new_height = round(new_width * height / width)
            new_image = img_pillow.resize((new_width, new_height), Image.LANCZOS)
            new_image.save(
                new_file_full_path,
                optimize=True,
                quality=70,
            )
            print(f'{file_full_path} convertido com sucesso !')
            exif = img_pillow._getexif()  # info das imagem, tem que armazenar e colocar de volta, senao: apagado
            new_image.close()
            img_pillow.close()


if __name__ == '__main__':
    main_images_folder = r'C:\Users\Martin Lucidarme\Pictures\image_python'
    main(main_images_folder, new_width=1920)
