import requests
from time import time

if __name__ == "__main__":
    response = requests.get("https://worldcup26.ir/get/teams").json()

    times = response.get("teams", [])

    print(type(times))

    for time in times:
        nome = time.get("name_en")
        print(nome)