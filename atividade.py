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

elif opcao == "2":
        if len(cadastro) == 0:
            print("Nenhum personagem cadastrado.")
        else:
            print("\n=== LISTA DE PERSONAGENS ===")
            for codigo, dados in cadastro.items():
                print(f"\nCódigo: {codigo}")
                print(f"Nome: {dados['nome']}")
                print(f"Classe: {dados['classe']}")
                print(f"Nível: {dados['nivel']}")
                print(f"Vida: {dados['vida']}")
                print(f"Mana: {dados['mana']}")

elif opcao == "3":
        codigo = input("Digite o código que deseja atualizar: ")

        if codigo not in cadastro:
            print("Código não encontrado.")
        else:
            print("Digite os novos dados:")
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

            print("Personagem atualizado!")