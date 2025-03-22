import os


#criar lista
restaurantes = []



def main():
    limpa_tela()
    titulo()   
    menu_principal()

def cadastrar_restaurante():
    limpa_tela()
    print('***Cadastro de Novos Restaurantes***\n')
    
    nome_fantasia = input('Digite o nome do restaurante que deseja cadastrar: \n')
    categoria = input('\nQual seguimento é este restautante?\n')

    dados_restaurante = {'nome_fantasia':nome_fantasia,'categoria':categoria,'ativo':False}



    restaurantes.append(dados_restaurante)
    print(f'\nO restaurante {nome_fantasia} foi cadastrado com sucesso.\n')
    input('Aperte ENTER para voltar ao menu principal')
    main()

def listar_restaurantes():
    limpa_tela()
    print('***Listando os restaurantes cadastrados***\n')
    #pra cada restaurante na lista restaurantes:

    for itens_na_lista in restaurantes:
        nome_fantasia = itens_na_lista['nome_fantasia']
        categoria = itens_na_lista['categoria']
        print(f'* Nome Fantasia: {nome_fantasia} \n* Categoria: {categoria} \n')
      
            
    input('Aperte ENTER para retornar ao menu')
    main()

def limpa_tela():
    os.system('clear')

def titulo():
    print('\nSabor Express\n')

def menu_principal():

    
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurantes')
    print('3. Sair\n')

    #tratar erros de digitação de opções (inputs)
    try:

        opcao = int(input('Escolha uma opção: '))
        match opcao:
            case 1:
                cadastrar_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                sair()
           
            case _:
                
                input('\nOpção Inválida. \nAperte ENTER e coloque novamente')
                
                main()
            

    except:
        
        input('Opção Inválida. \nAperte ENTER e coloque novamente')
        limpa_tela()
        menu_principal()

def sair():
    limpa_tela()
 
if __name__ == '__main__':
    main()