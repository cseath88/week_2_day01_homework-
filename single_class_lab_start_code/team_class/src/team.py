class Team:
    def __init__(self, input_team_name, input_players, input_coach):
        self.name = input_team_name
        self.players = input_players
        self.coach = input_coach

    def get_team_name(self):
        return self.name
    
    def get_team_total(self):
        return len(self.players)
    
    def get_coach_name(self):
        return self.coach
    
    def add_player(self, new_player):
        self.players.append(new_player)

    def has_player(self, player_search):
        for player in self.players:
            if player == player_search:
                return True
            
        return False
    
    
