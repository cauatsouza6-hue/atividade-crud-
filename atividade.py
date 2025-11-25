Herois = {
    "sh001":{
    "nome": "homem-aranha",
    "identidade": "piter parck",
    "nivel de poder": [200],
    "universo": "marvel",
}} 

while True:
    print("\n1- cadrastar")  
    print("2- listar")  
    print("3- atualizar")  
    print("4- remover")  
    print("5- sair") 
    opcao = input("escolha uma opção:")
    if opcao == "1":
        codigo  = input(f"seu personagem é Heroi ou vilao:")
        if nome  in opcao:
            print("essa opcao já existie!")
            nome = input("nome do personagens:")
            identidade = input("qual é a sua indentidade secreta:")
            nivel = input("pontos de vida do personagens:")
            universo = input("qual universo:")
            [codigo] = {