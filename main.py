# This is a sample Python script.
from Role import Role
import random

# makes the member list with commas separating each member
def make_memberlist():
    longlist = str(input("Please paste everyone's names ensuring each name is separated by a comma (,)\n"))
    return longlist.split(",")

# creates finallist in main where the list returned contains members with groups of True and False values
def make_memberlist_with_role_class(memberlist,team):
    memberlist_final = []
    for x in memberlist:
        memberlist_final.append(Role(x, team))
    return memberlist_final

# randomizes the list and then splits the list of names into 2 teams
def split_into_teams(list):
    random.shuffle(list)
    half = len(list) // 2
    return list[:half], list[half:]

# takes a team's list and a special role then turns a regular member of that team into the special role
def pick_special_role(team_list,role):
    member = random.choice(team_list)
    while member.role != "Regular Member":
        member = random.choice(team_list)
    Role.change_role(member,role)
    return None

# writes a txt file that displays a team's members and the member's roles
def display_team(team_list,file_name):
    file = open(file_name,"w")
    for x in team_list:
        file.write(x.team_info() + "\n")
    file.close()
    return None

# standard game that adds Bomber and President
def round_1(red_team,blue_team):
    pick_special_role(red_team,"Bomber")
    pick_special_role(blue_team,"President")

    return red_team, blue_team

# Game introduces spies and coy roles
def round_2(red_team,blue_team):
    pick_special_role(red_team,"Bomber")
    pick_special_role(blue_team,"President")
    pick_special_role(red_team, "Red Spy")
    pick_special_role(blue_team, "Blue Spy")
    pick_special_role(red_team, "Red Coy")
    pick_special_role(blue_team, "Blue Coy")

    return red_team, blue_team

# Game introduces Engineer and Doctor roles
def round_3(red_team,blue_team):
    pick_special_role(red_team,"Bomber")
    pick_special_role(blue_team,"President")
    pick_special_role(red_team, "Red Spy")
    pick_special_role(blue_team, "Blue Spy")
    pick_special_role(red_team, "Red Coy")
    pick_special_role(blue_team, "Blue Coy")
    pick_special_role(red_team, "Engineer")
    pick_special_role(blue_team, "Doctor")

    return red_team, blue_team

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Creates the Blue and Red Teams
    member_list = make_memberlist()
    team1, team2 = split_into_teams(member_list)
    blue_team = make_memberlist_with_role_class(team1,"Blue")
    red_team = make_memberlist_with_role_class(team2,"Red")

    # Asks what version user wants to play
    round = input("Which round is it?\n")

    if round == "1":
        red_team, blue_team = round_1(red_team,blue_team)
    if round == "2":
        red_team, blue_team = round_2(red_team,blue_team)
    if round == "3":
        red_team, blue_team = round_3(red_team,blue_team)

    # Writes roles out on files so they are easily accessible outside of IDE
    display_team(blue_team,"Blue Team List.txt")
    display_team(red_team,"Red Team List.txt")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
