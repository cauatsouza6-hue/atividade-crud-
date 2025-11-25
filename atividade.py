cadastro = {}

while True:
    print("\n===== MENU =====")
    print("1 - Cadastrar personagem")
    print("2 - Listar personagens")
    print("3 - Atualizar personagem")
    print("4 - Remover personagem")
    print("5 - Sair")
    
    opcao = input("Escolha uma opção: ")

if opcao == "1":
        codigo = input("Código do personagem (ex: p001): ")

        if codigo in cadastro:
            print("Este código já existe!")
        else:
            nome = input("Nome: ")
            classe = input("Classe: ")
            nivel = input("Nível: ")
            vida = input("Vida: ")
            mana = input("Mana: ")

            cadastro[codigo] = {
                "nome": nome,
                "classe": classe,
                "nivel": nivel,
                "vida": vida,
                "mana": mana
            }

            print("Personagem cadastrado com sucesso!")