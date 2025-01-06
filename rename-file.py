import os
import numpy as np
from progress.bar import Bar

# Array com os nomes a serem renomeados, lembrando que a quantidade de nomes precisa ser igual a quantidade de pastas e no caso dos array o ultimo é o primeiro
# lista_sem_extensoes = ["isso-ai-gran", "hehe-gran", "parabens-gran", "sucesso-gran", "se-e-bom-mesmo-gran", "legal-ein-gran", "oloco-gran", "que-isso-gran", "foda-ein-gran"]  # Atualize essa lista conforme necessário


# Colocar aqui o caminho da pasta com os artigos
pathBaseName = "E:/Area de Trabalho/teste-pasta-base"
BaseNameFilesList = os.listdir(pathBaseName)
BaseNameFilesArray = np.array(BaseNameFilesList)
lista_sem_extensoes = [nome[:-4] if nome.endswith('.jpg') or nome.endswith('.webp') or nome.endswith('.png') or nome.endswith('.php') or nome.endswith('.jpeg') else nome for nome in BaseNameFilesArray]

# Aqui fica a lista em Array com os nomes que irão renomear as fotos
print(lista_sem_extensoes)

# Aqui devera ficar as fotos dos artigos, colocar em ordem de igual ao dos artigos
pathNewName = "E:/Area de Trabalho/teste-pasta"
NewNameFiles = os.listdir(pathNewName)

# Esse script roda APENAS se a quantidade de nomes no Array for a mesma quantidade de arquivos na pasta de fotos
if len(NewNameFiles) == len(lista_sem_extensoes):
    # Criando a barra de progresso
    bar = Bar('Renomeando arquivos', max=len(NewNameFiles))

    # Iterando sobre os arquivos e renomeando
    for i in range(len(NewNameFiles)):
        # Caminho completo para o arquivo original
        arquivo_antigo = os.path.join(pathNewName, NewNameFiles[i])
        
        # Obtendo a extensão do arquivo original
        nome_base, extensao = os.path.splitext(NewNameFiles[i])

        # Garantir que o novo nome não tenha ponto extra no final
        novo_nome = lista_sem_extensoes[i].rstrip('.')  # Remove qualquer ponto final
        
        # Concatenando o novo nome com a extensão original
        arquivo_novo = os.path.join(pathNewName, novo_nome + extensao)

        # Renomeando o arquivo
        os.rename(arquivo_antigo, arquivo_novo)
        
        # Atualizando a barra de progresso
        bar.next()

    # Finalizando a barra de progresso
    bar.finish()
else:
    print("A quantidade de arquivos e nomes não é igual!")
