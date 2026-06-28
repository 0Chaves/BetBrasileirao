from models.persist.conexao_bd import conexao
from models.persist.team_dao import TeamDAO
from models.team import Team

if __name__ == "__main__":
    # conexao.conectar()
    # conexao.criar_banco()
    teamA = Team(nome="Interrrr", vitorias=0, derrotas=0, empates=0)
    teamDao = TeamDAO()
    teamDao.inserir(teamA)
    opt = 0
    while opt != 5:
        print("""
1- Inserir
2- Deletar
3- Atualizar
4- Pesquisar
""")
        opt = int(input("Selecione uma opcao: "))
        match opt:
            case 1:
                nome = input("Digite o nome do time: ")
                vitorias = int(input("Quantidade de vitorias: "))
                derrotas = int(input("Quantidade de derrotas: "))
                empates = int(input("Quantidade de empates: "))
                team = Team(nome=nome, vitorias=vitorias, derrotas=derrotas, empates=empates)
                teamDao.inserir(team)
            case 4:
                id = int(input("Qual o id: "))
                team = teamDao.pesquisar(id)
                print(team)