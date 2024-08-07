for i in range(10):
    if i == 2 or i == 4 or i == 6:
        print(f'i é {i}, pulando...')
        continue

    if i == 8:
        print('i é 8, seu else não executará')
        break

    for j in range(1, 4):
        print(i, j)
else:
    print('For completo com sucesso!')
