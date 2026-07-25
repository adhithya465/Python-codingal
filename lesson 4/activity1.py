name=input("Enter your real name, Agent: ")
gadget=input("Enter your favorite gadget: ")
agent_number=7
speed_rating=9.5
mission_count=12
height_m=1.65
is_active=True
print("Name: ",name, "-> type: ",type(name))
print("Gadget: ",gadget, "-> type: ", type(gadget))
print("Agent Number ",agent_number, "-> type: ", type(agent_number))
print("Speed Rating ",speed_rating,"->type: ", type(speed_rating))
print("Mission Count ",mission_count,"-> type: ",type(mission_count))
print("Height (m) ",height_m,"-> type: ",type(speed_rating))
print("Is Active ",is_active, "-> type: ",type(is_active))
agent_number_str=str(agent_number)
speed_rating_str=str(speed_rating)
mission_count_str=str(mission_count)
height_m_str=str(height_m)
is_active_str=str(is_active)
print("Agent Number in text",agent_number_str, "-> type: ", type(agent_number_str))
print("Speed Rating in text",speed_rating_str,"->type: ", type(speed_rating_str))
print("Mission Count in text",mission_count_str,"-> type: ",type(mission_count_str))
print("Height (m): in text ",height_m_str,"-> type: ",type(speed_rating_str))
print("Is Active in text",is_active_str, "-> type: ",type(is_active_str))

first_three = name[0:3]
last_letter = name[-1]
code_name = first_three + last_letter
print("First 3 letters of name:", first_three)
print("Last letter of name:", last_letter)
print("Secret Code Name:", code_name)

reversed_gadget = gadget[::-1]
print("Reversed Gadget Name:", reversed_gadget)


badge_line_1 = "AGENT " + code_name.upper()
badge_line_2 = "ID: " + agent_number_str + " | MISSIONS: " + mission_count_str
badge_line_3 = "SPEED: " + speed_rating_str + " | ACTIVE: " + is_active_str
badge_line_4 = "SECRET GADGET CODE: " + reversed_gadget.upper()

print("")
print("===== SECRET AGENT BADGE =====")
print(badge_line_1)
print(badge_line_2)
print(badge_line_3)
print(badge_line_4)
print("===============================")
