# PART 1: Ask the player for their details
name = input("Enter your real name, Player: ")
team = input("Enter your favorite basketball team: ")

# PART 2: Store the player's details using different data types
jersey_number = 30
points_per_game = 28.5
championships = 4
practice_hours = 2.5
is_starter = True

# PART 3: Print each detail along with its data type
print("Name:", name, "-> type:", type(name))
print("Favorite Team:", team, "-> type:", type(team))
print("Jersey Number:", jersey_number, "-> type:", type(jersey_number))
print("Points Per Game:", points_per_game, "-> type:", type(points_per_game))
print("Championships:", championships, "-> type:", type(championships))
print("Practice Hours:", practice_hours, "-> type:", type(practice_hours))
print("Starter:", is_starter, "-> type:", type(is_starter))

# PART 4: Typecast the numbers and true/false value into text
jersey_text = str(jersey_number)
championships_text = str(championships)
points_text = str(points_per_game)
starter_text = str(is_starter)

print("Jersey Number as text:", jersey_text, "-> type:", type(jersey_text))
print("Championships as text:", championships_text, "-> type:", type(championships_text))
print("Points as text:", points_text, "-> type:", type(points_text))
print("Starter as text:", starter_text, "-> type:", type(starter_text))

# PART 5: Slice the name to create a player code
first_three = name[0:3]
last_letter = name[-1:]
player_code = first_three + last_letter

print("First 3 letters of name:", first_three)
print("Last letter of name:", last_letter)
print("Player Code:", player_code)

# PART 6: Reverse the team name using slicing
reversed_team = team[::-1]
print("Reversed Team Name:", reversed_team)

# PART 7: Join everything together to build the final player card
card_line_1 = "BASKETBALL PLAYER " + player_code.upper()
card_line_2 = "JERSEY: " + jersey_text + " | CHAMPIONSHIPS: " + championships_text
card_line_3 = "POINTS: " + points_text + " | STARTER: " + starter_text
card_line_4 = "SECRET TEAM CODE: " + reversed_team.upper()

# PART 8: Print the complete basketball player card
print("")
print("===== BASKETBALL PLAYER CARD =====")
print(card_line_1)
print(card_line_2)
print(card_line_3)
print(card_line_4)
print("=================================")