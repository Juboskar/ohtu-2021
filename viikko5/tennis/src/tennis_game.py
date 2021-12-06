class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.players = {player1_name: 0, player2_name: 0}

    def won_point(self, player_name):
        self.players[player_name] += 1


    def get_score(self):
        scores = ["Love", "Fifteen", "Thirty", "Forty"]
        score1 = list(self.players.values())[0]
        score2 = list(self.players.values())[1]

        if score1 == score2:
            return f"{scores[score1]}-All" if score1 < 4 else "Deuce"

        elif max(list(self.players.values())) >= 4:
            max_player = list(self.players)[0] if score1 > score2 else list(self.players)[1]

            minus_result = abs(score1 - score2)
            if minus_result == 1:
                return f"Advantage {max_player}"
            elif minus_result >= 2:
                return = f"Win for {max_player}"   
        
        else:
            return f"{scores[score1]}-{scores[score2]}"
