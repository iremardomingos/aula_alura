import os
os.system('clear')


livros = [
    {"nome": "1984", "estoque": 0},
    {"nome": "Dom Casmurro", "estoque": 0},
    {"nome": "O Pequeno Príncipe", "estoque": 0},
    {"nome": "O Hobbit", "estoque": 1},
    {"nome": "Orgulho e Preconceito", "estoque": 0}
]

print('*** LIVROS DISPONIVEIS:***')
print()

for livro in livros:
    if livro ['estoque'] == 0:
        continue
    
    print(f'Livro Disponível: {livro['nome']}')
  
print()



