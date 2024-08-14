# tupla
chaves = ('Nome','Idade','Profissao')


# LISTA de dicionario
usuarios = [
    {
    chaves[0]: 'fulano',
    chaves[1]: '20',
    chaves[2]: 'programador'
    },
    {
     chaves[0]: 'Cicrano',
     chaves[1]: '35',
    chaves[2]: 'Analista'
    },
    {
    chaves[0]: 'Beltano',
    chaves[1]: '45',
    chaves[2]: 'Faxineiro'
    }
]




# exibe minha lista de dicionario
print(f'{'='*10} LISTA DE USUARIOS {'='*10}\n')

for usuario in usuarios:
     for chave in chaves:
        print(f'{chave}: {usuario[chave]}')

     print(f'\n{'='*10}\n')

# adcionador novo dicionario a lista
usuario = {}

for i in range(len(chaves)):
    usuario[chaves[i]] = input(f'informe {chaves[i]}: ')

usuarios.append(usuario)
print(f'\nUsuario cadastrado com sucesso!')

print(f'\n{'='*10} LISTA DE USUARIOS {'='*10}\n')

for usuario in usuarios:
    for chave in chaves:
        print(f'{chave}: {usuario[chave]}')

    print(f'\n{'-'*10}\n')


