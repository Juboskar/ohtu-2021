import requests
from player import Player
from datetime import datetime

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    response = requests.get(url).json()

    # print("JSON-muotoinen vastaus:")
    # print(response)

    players = []

    for player_dict in response:
        
        player = Player(
            player_dict['name'], 
            player_dict['nationality'],
            player_dict['assists'],
            player_dict['goals'],
            player_dict['penalties'],
            player_dict['team'],
            player_dict['games']
        )
        players.append(player)

    print(f"Players from FIN {datetime.now()}:\n")

    for player in sorted(
        filter(lambda p: p.nationality=='FIN', players), 
        key=lambda x: x.goals + x.assists, reverse=True
        ):
        print(player)

if __name__ == "__main__":
    main()
