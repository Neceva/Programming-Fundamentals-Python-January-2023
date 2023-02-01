first_team_a = ["A-1", "A-2", "A-3", "A-4", "A-5", "A-6", "A-7", "A-8", "A-9", "A-10", "A-11"]
second_team_b = ["B-1", "B-2", "B-3", "B-4", "B-5", "B-6", "B-7", "B-8", "B-9", "B-10", "B-11"]

game_is_terminated = False
players = input().split()

for player in players:
    if player in first_team_a:
        first_team_a.remove(player)
    elif player in second_team_b:
        second_team_b.remove(player)
    if len(first_team_a) < 7 or len(second_team_b) < 7:
        game_is_terminated = True
        break

print(f"Team A - {len(first_team_a)}; Team B - {len(second_team_b)}")

if game_is_terminated:
    print("Game was terminated")
