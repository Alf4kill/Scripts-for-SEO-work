from PIL import Image
import os

def convert_to_webp(input_folder, output_folder):
    """
    Converte arquivos .png e .jpg em um diretório para o formato .webp.

    Args:
        input_folder (str): Caminho do diretório com os arquivos de entrada.
        output_folder (str): Caminho do diretório para salvar os arquivos .webp.
    """
    # Garantir que o diretório de saída exista
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterar sobre os arquivos no diretório de entrada
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.webp")

            try:
                # Abrir a imagem e convertê-la para .webp
                with Image.open(input_path) as img:
                    img.save(output_path, format="WEBP")
                    print(f"Convertido: {input_path} -> {output_path}")
            except Exception as e:
                print(f"Erro ao converter {input_path}: {e}")

if __name__ == "__main__":
    # Diretórios de exemplo
    input_folder = "E:/Area de Trabalho/teste-pasta-base"
    output_folder = "E:/Area de Trabalho/teste-final"

    convert_to_webp(input_folder, output_folder)
