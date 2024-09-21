from PIL import Image
from os import chdir, listdir

chdir('C:/Users/gustavo.nunes/Desktop/Croquis')
arquivos = listdir()
print(arquivos)

for z in range(len(arquivos)):

    source_image = Image.open('C:/Users/gustavo.nunes/Desktop/Croquis/' + arquivos[z])
    source_image = source_image.convert('RGBA')
    height, width = source_image.size

    new_image = Image.new('RGBA', (width, height))

    source_pixels = source_image.load()
    new_pixels = new_image.load()

    for x in range(width):
        for y in range(height):
            rgba = source_pixels[x, y]
            new_pixels[x, y] = rgba

    new_image.save('C:/Users/gustavo.nunes/Desktop/Croqui_sem_fundo/' + arquivos[z])

print("Processo finalizado!")