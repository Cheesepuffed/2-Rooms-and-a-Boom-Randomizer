class Role:
    def __init__(self, name, team):
        self.name = name
        self.team = team
        self.role = "Regular Member"

    def change_role(self,role):
        self.role = role

    def team_info(self):
        return self.name + "\nRole: " + self.role + "\nTeam: " + self.team + "\n"