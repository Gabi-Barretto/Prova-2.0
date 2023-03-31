from models.games import iniciar_banco_de_dados, adicionar_games, listar_games

if __name__ == '__main__':
    #Iniciando o banco e o session
    Session = iniciar_banco_de_dados()
    session = Session()

# Condicoes para adicionar e listar os games
    while True:
        print("1. Adicionar Games (Nome, Plataforma, Preço, Quantidade)")
        print("2. Listar Games")
        print("3. Sair")
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            nome = input("Nome do Jogo: ")
            plat = input("Plataforma: ")
            preco = input("Preço: ")
            qnt = input("Quantidade: ")
            adicionar_games(session, nome, plat, preco, qnt)
        elif opcao == 2:
            games = listar_games(session)
            for game in games:
                print(f"{game.id}. {game.name} - {game.plat} - {game.preco} - {game.qnt}")
        elif opcao == 3:
            break
        else:
            print("Opção inválida")