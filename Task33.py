team_count = 3
players_count = 4
team_results = []
 
max_team_number = winner_number = max_result = 0
for team_number in range(1, team_count+1):
    team_result = []
    max_for_player = max_player_number = 0
 
    for player_number in range(1, players_count + 1):
        player_score = input("Enter {} team {} player result: ".format(
            team_number,
            player_number,
        )).split()
        player_sum = sum([int(score) for score in player_score])
        if player_sum > max_for_player:
            max_for_player, max_player_number = player_sum, player_number
 
    print("Team {}. The winner is the player {} with the score of {}".format(
        team_number,
        max_player_number,
        max_for_player,
    ))
 
    if max_for_player > max_result:
        max_team_number, winner_number = team_number, max_player_number
        max_result = max_for_player
 
print("The best result was shown by player {} of the team {} with the score of {}".format(
    winner_number,
    max_team_number,
    max_result,
))