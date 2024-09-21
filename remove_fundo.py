# Importing Required Modules
from rembg import remove
from PIL import Image
from os import chdir, listdir

chdir('C:/Users/gustavo.nunes/Desktop/Croquis')
arquivos = listdir()
print(arquivos)

for x in range(len(arquivos)):

    input_path = 'C:/Users/gustavo.nunes/Desktop/Croquis/' + arquivos[x]
    output_path = 'C:/Users/gustavo.nunes/Desktop/Croqui_sem_fundo/' + arquivos[x]

    input = Image.open(input_path)
    output = remove(input)
    output.save(output_path)

print("Processo finalizado!")