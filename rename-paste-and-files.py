import os
import numpy as np
from progress.bar import Bar

# Array com os nomes a serem renomeados, lembrando que a quantidade de nomes precisa ser igual a quantidade de pastas e no caso dos array o ultimo é o primeiro
# lista_sem_extensoes = ["isso-ai-gran", "hehe-gran", "parabens-gran", "sucesso-gran", "se-e-bom-mesmo-gran", "legal-ein-gran", "oloco-gran", "que-isso-gran", "foda-ein-gran"]  # Atualize essa lista conforme necessário


# Caminho com os artigos que serão usados para renomear as pastas e arquivos
path_base = "E:/Area de Trabalho/teste-pasta-base"
BaseNameFilesList = os.listdir(path_base)
BaseNameFilesArray = np.array(BaseNameFilesList)

# Isso aqui esta removendo as extensoes dentro do array
lista_sem_extensoes = [
    nome[:-4] if nome.endswith(('.jpg', '.webp', '.png', '.php', '.jpeg')) else nome
    for nome in BaseNameFilesArray
]

# print com a lista
print(lista_sem_extensoes)

# Caminho aonde ira ficar as pastas com arquivos
pathNewName = "E:/Area de Trabalho/teste-pasta"
NewNameFiles = os.listdir(pathNewName)

# Verificar se a quantidade de pastas corresponde à lista de novos nomes
pastas = [pasta for pasta in os.listdir(pathNewName) if os.path.isdir(os.path.join(pathNewName, pasta))]
if len(pastas) == len(lista_sem_extensoes):
    # Barra de progresso
    bar = Bar('Renomeando pastas e arquivos', max=len(pastas))
    
    for idx, pasta in enumerate(pastas):
        caminho_pasta_antiga = os.path.join(pathNewName, pasta)
        
        # Garantir que o nome não tenha ponto extra no final (Importante para os arquivos .webp)
        novo_nome_pasta = lista_sem_extensoes[idx].rstrip('.')
        caminho_pasta_nova = os.path.join(pathNewName, novo_nome_pasta)
        
        # Obter lista de arquivos dentro da pasta
        arquivos = os.listdir(caminho_pasta_antiga)
        
        # Renomear arquivos dentro da pasta
        for i, arquivo in enumerate(arquivos):
            caminho_arquivo_antigo = os.path.join(caminho_pasta_antiga, arquivo)
            nome_base, extensao = os.path.splitext(arquivo)
            
            # Garantir que o nome do arquivo não tenha ponto extra no final (Importante para os arquivos .webp)
            novo_nome_arquivo = f"{novo_nome_pasta}-{i+1}".rstrip('.') + extensao
            caminho_arquivo_novo = os.path.join(caminho_pasta_antiga, novo_nome_arquivo)
            os.rename(caminho_arquivo_antigo, caminho_arquivo_novo)
        
        # Renomear a própria pasta após renomear os arquivos
        os.rename(caminho_pasta_antiga, caminho_pasta_nova)
        
        bar.next()
    bar.finish()
else:
    print("A quantidade de pastas e nomes não é igual!")
