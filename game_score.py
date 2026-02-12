player_name = input("Enter the player name:")
games_played = int(input("enter the how many games played in number: "))
total_score = int(input("enter the total score for all games in number:"))
if games_played > 0:
    average_score = total_score / games_played
else:
    average_score =0
print("\n----Games Summary of player---")
print("player name :" ,player_name)
print ("Games played:" ,games_played)
print("Total score:",total_score)
print("Average Score:" , average_score)