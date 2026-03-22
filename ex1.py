# Importa a classe Path da biblioteca pathlib
# pathlib é uma forma moderna e mais intuitiva de trabalhar com arquivos e diretórios
from pathlib import Path

# Cria um objeto Path que representa o caminho para o arquivo "files/abc.txt"
# Não cria o arquivo ainda, apenas representa o caminho
file_01 = Path('files/abc.txt')

# Mostra o tipo da variável (vai ser <class 'pathlib.PosixPath'> ou WindowsPath)
# Isso ajuda a entender que estamos lidando com um objeto e não uma string comum
print(type(file_01))

# Verifica se o arquivo realmente existe no sistema
if file_01.exists():

    # Abre o arquivo no modo 'w' (write = escrita)
    # Se o arquivo existir, ele será SOBRESCRITO
    # O "with" garante que o arquivo será fechado automaticamente depois
    with open(file_01, 'w') as file:

        # Escreve o texto "Content!" dentro do arquivo
        file.write('Content!')

else:
    # Caso o arquivo não exista, exibe essa mensagem
    print('File does not exist')   

# Mostra apenas o nome do arquivo com extensão (abc.txt)
print("file name:", file_01.name)

# Mostra o nome do arquivo SEM a extensão (abc)
# Muito útil quando você precisa manipular nomes dinamicamente
print("file stem:", file_01.stem)

# Mostra apenas a extensão do arquivo (.txt)
# Útil para validar tipos de arquivos em sistemas reais
print("file suffix:", file_01.suffix)

# ------------------------------------ PART 02 ------------------------------------

# Cria um objeto Path representando o diretório "files"
# Aqui não é um arquivo, e sim uma pasta
path = Path('files')

# Lista todos os arquivos e diretórios dentro de "files"
# iterdir() retorna um "iterador" com objetos Path
# Cada item representa um arquivo ou subpasta dentro do diretório
print(list(path.iterdir()))