import requests

url = "https://api.football-data.org/v4/competitions/BSA/standings"

payload={}
headers = {
  'X-Auth-Token': 'a7a49ca8c1374bd9865710b3d6da0329',
}

standings_response = requests.request("GET", url, headers=headers, data=payload).json()

print(standings_response["standings"][0]["table"][0])

def create_admin():
    pass

admin_auth = "bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiZXhwIjoxNzg2NzI3NDEyLCJpc0FkbWluIjp0cnVlfQ.qc7rqXdg_QSqFnl6ViAYhOAw1qni2I-zF0drHix2s2A"

def first_sync_teams():
    
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
        
        headers = {
            "Authorization": admin_auth
        }
        post_response = requests.post("http://localhost:8000/teams", json=payload, headers=headers)

        if post_response.status_code == 401:
            print("Não autorizado")
            break
        print("Team saved")
        print({post_response.status_code})

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

def sincronizar_placares():
    pass

if __name__ == "__main__":
    first_sync_teams()
    # sync_teams()