import requests
from models.team import Team
from models.persist.team_dao import TeamDAO

teamDao = TeamDAO()

def sincronizar_times():
    response = requests.get("https://worldcup26.ir/get/teams").json()

    times = response.get("teams", [])
    times = sorted(times, key=lambda x: int(x['id']))
    total = len(times)
    print(total)
    print(type(times))

    for time in times:
        nome = time.get("name_en")
        bandeira = time.get("flag")
        sigla = time.get("fifa_code")
        grupo = time.get("groups")
        id = time.get("id")
        # print(nome, bandeira, sigla, grupo)
        team = Team(nome=nome, bandeira=bandeira, sigla=sigla, grupo=grupo)
        teamDao.inserir(team)
        print(f"Time: {nome} Salvo com sucesso.")

def sincronizar_placares():
    pass

if __name__ == "__main__":
    sincronizar_times()