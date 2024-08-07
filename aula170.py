# os.listdir para navegar em caminhos
# C:\Users\erick\OneDrive\Documentos\Udemy\Python\EXEMPLO 
import os
os.system('cls')
# caminho = r'C:\\Users\\erick\\OneDrive\\Documentos\\Udemy\\Python\\EXEMPLO'
caminho = os.path.join('C:\\Users', 'erick', 'OneDrive', 'Documentos', 'Udemy', 'Python', 'EXEMPLO')
# print(caminho)

for pasta in os.listdir(caminho):
    caminho_completo_pasta = os.path.join(caminho, pasta)
    print('>', pasta)

    # Checando se é um diretório
    if not os.path.isdir(caminho_completo_pasta):
        continue
    
    for item in os.listdir(caminho_completo_pasta):
        print('    -', item)
    
    print()
