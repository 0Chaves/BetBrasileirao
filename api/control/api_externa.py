import requests
import concurrent.futures

url = "https://api.football-data.org/v4/competitions/BSA/standings"
url_matches = "https://api.football-data.org/v4/competitions/BSA/matches"

payload={}
headers = {
  'X-Auth-Token': 'a7a49ca8c1374bd9865710b3d6da0329',
}

standings_response = requests.request("GET", url, headers=headers, data=payload).json()

matches_response = requests.request("GET", url_matches, headers=headers, data=payload).json()

# print(standings_response["standings"][0]["table"][0])

def create_admin():
    pass

admin_auth = "bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiZXhwIjoxNzg2ODAzODExLCJpc0FkbWluIjp0cnVlfQ.aIIoBVE8-CCqaRmVRC0wrXSRTxBqo6fcxHnNAl-hIQ4"

def save_team(team): 
    payload = {
        "id": team["team"]["id"],
        "name": team["team"]["shortName"],
        "flag": team["team"]["crest"],
        "code": team["team"]["tla"],
        "position": team["position"],
        "playedGames": team["playedGames"],
        "won": team["won"],
        "draw": team["draw"],
        "lost": team["lost"],
        "points": team["points"]
    }
    
    headers = {
        "Authorization": admin_auth
    }
    post_response = requests.post("http://localhost:8000/teams", json=payload, headers=headers)

    print({post_response.status_code})
    return post_response.status_code

def sync_teams_paralelo():
    teams = standings_response["standings"][0]["table"]
    print(f"Sincronizando {len(teams)} times")

    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        resultados = list(executor.map(save_team, teams))
        
    print(f"Sincronização concluída. {resultados.count(201)} inseridos com sucesso.")

    
def sync_teams():
    
    teams = standings_response["standings"][0]["table"]
    total = len(teams)
    print(total)

    for team in teams:
        payload = {
            "id": team["team"]["id"],
            "name": team["team"]["shortName"],
            "flag": team["team"]["crest"],
            "code": team["team"]["tla"],
            "position": team["position"],
            "playedGames": team["playedGames"],
            "won": team["won"],
            "draw": team["draw"],
            "lost": team["lost"],
            "points": team["points"]
        }

        # team_to_change = requests.get(f"http://localhost:8000/teams/name/{payload["name"]}").json()

        headers = {
            "Authorization": admin_auth
        }
        post_response = requests.put(f"http://localhost:8000/teams/{payload["id"]}", json=payload, headers=headers)

        if post_response.status_code == 401:
            print("Não autorizado")
            break
        print("Team saved")
        print({post_response.status_code})

def save_match(match):
    date = match["utcDate"].split("T")[0]
    winner_id = None
    if match["score"]["winner"] == "HOME_TEAM":
        winner_id = match["homeTeam"]["id"]
    elif match["score"]["winner"] == "AWAY_TEAM":
        winner_id = match["awayTeam"]["id"]
    payload = {
        "id": match["id"],
        "status": match["status"],
        "date": date,
        "home_team_goals": match["score"]["fullTime"]["home"],
        "away_team_goals": match["score"]["fullTime"]["away"],
        "winner_str": match["score"]["winner"],
        "home_team_id": match["homeTeam"]["id"],
        "away_team_id": match["awayTeam"]["id"],
        "winner_id": winner_id,
    }
    
    headers = {
        "Authorization": admin_auth
    }
    post_response = requests.post("http://localhost:8000/games", json=payload, headers=headers)

    print(post_response.status_code)
    if post_response.status_code == 422:
        print("Erro no seguinte jogo:")
        print(payload)
    return post_response.status_code

def sync_matches_paralelo():
    matches = matches_response["matches"]
    print(f"Sincronizando {len(matches)} jogos")

    # max_workers = requisições simultâneas
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        resultados = list(executor.map(save_match, matches))
        
    print(f"Sincronização concluída. {resultados.count(201)} inseridos com sucesso.")

if __name__ == "__main__":
    sync_teams_paralelo()
    # sync_teams()
    sync_matches_paralelo()