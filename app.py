import os
restaurantes = []

def exibir_nome_programa():
    print("𝑆𝑎𝑏𝑜𝑟 𝐸𝑥𝑝𝑟𝑒𝑠𝑠\n")

def exibir_opcoes():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurante")
    print("3. Ativar restaurante")
    print("4. Sair\n")

def cadastro_restaurante():
    os.system('cls')
    print('Cadastro de novos restaurantes\n')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_restaurante)
    print(f'Parabéns! O restaurante {nome_restaurante} foi cadastrado com sucesso!\n')
    voltar_ao_menu()

def voltar_ao_menu():
    input('Digite qualquer tecla para voltar ao menu ')
    main()

def finalizar_app():
    os.system('cls')
    print("Encerrando o Programa\n")

def opcao_invalida():
    os.system('cls')
    print("Opção Inválida!")
    voltar_ao_menu()

def escolher_opcoes():
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))
        if opcao_escolhida == 1:
            cadastro_restaurante()
        elif opcao_escolhida == 2:
            print("Listar Restaurante")
        elif opcao_escolhida == 3:
            print("Ativar Restaurante")
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()