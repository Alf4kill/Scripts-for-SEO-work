from PIL import Image
import os

def convert_and_rename_images_in_subfolders(base_folder):
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
                            img = img.convert("RGB")
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
base_folder = "E:/Area de Trabalho/pasta-para-renomear"
convert_and_rename_images_in_subfolders(base_folder)
