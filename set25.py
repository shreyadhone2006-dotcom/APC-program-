user1 = {"Shreya","Gauri","Ishita","Shreyac","Dhiraj"}
user2 = {"Shreya","Ishita","Dhiraj","Dipali"}

print("Mutual friends:", user1 & user2)
print("User 1 only:", user1 - user2)
print("User 2 only:", user2 - user1)
print("Total unique friends:", len(user1 | user2))