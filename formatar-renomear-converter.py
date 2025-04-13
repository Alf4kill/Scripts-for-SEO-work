from PIL import Image
import os

def crop_center(img, crop_width, crop_height):
    img_width, img_height = img.size
    left = (img_width - crop_width) // 2
    top = (img_height - crop_height) // 2
    right = left + crop_width
    bottom = top + crop_height
    return img.crop((left, top, right, bottom))

def resize_and_rename_images_in_subfolders(base_folder, width, height):
    if not os.path.exists(base_folder):
        print("A pasta base especificada não existe.")
        return

    for subfolder in os.listdir(base_folder):
        subfolder_path = os.path.join(base_folder, subfolder)
        if os.path.isdir(subfolder_path):
            count = 1
            for file_name in os.listdir(subfolder_path):
                input_path = os.path.join(subfolder_path, file_name)

                if os.path.isfile(input_path):
                    try:
                        with Image.open(input_path) as img:
                            img_ratio = img.width / img.height
                            target_ratio = width / height

                            # Redimensiona mantendo proporcao para depois cortar
                            if img_ratio > target_ratio:
                                new_height_temp = height
                                new_width_temp = int(height * img_ratio)
                            else:
                                new_width_temp = width
                                new_height_temp = int(width / img_ratio)

                            img = img.resize((new_width_temp, new_height_temp), Image.LANCZOS)
                            img = crop_center(img, width, height)

                            new_name = f"{subfolder}-{count}.webp"
                            output_path = os.path.join(subfolder_path, new_name)
                            img.save(output_path, "WEBP")
                            print(f"Imagem salva em: {output_path}")
                            count += 1
                        if input_path != output_path:
                            os.remove(input_path)
                    except Exception as e:
                        print(f"Erro ao processar a imagem {file_name}: {e}")

# Exemplo de uso
base_folder = "E:/Area de Trabalho/pasta-para-renomear-e-formatar"
new_width = 160
new_height = 250

resize_and_rename_images_in_subfolders(base_folder, new_width, new_height)
