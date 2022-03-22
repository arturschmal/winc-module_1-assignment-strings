# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

# Part 1
player_scored_1 = "Ruud Gullit"
player_scored_2 = "Marco van Basten"

goal_0 = 32
goal_1 = 54
scorers = player_scored_1 + " " + str(goal_0) + ", " + player_scored_2 + " " + str(goal_1)
report = (f'{player_scored_1} scored in the {goal_0}nd minute\n{player_scored_2} scored in the {goal_1}th minute')

# Part 2
player = "Ronald Koeman"

first_name = player[0:player.find(" ")]
print(first_name)

last_name_len = len(player[player.find(" ")+1:])
print(last_name_len)

name_short = f'{player[0]}. {player[player.find(" ")+1:]}'
print(name_short)

chant = int(len(first_name)-1) * f'{first_name}! ' + f'{first_name}!'
print(chant)

good_chant = chant[-1] != " "
print(good_chant)