morning = {"Gauri", "Sayali", "Shreya", "Ishita"}
afternoon = {"Shreya", "Gauri", "Shreya", "Minal"}

print("Both:", morning & afternoon)
print("Only morning:", morning - afternoon)
print("Only afternoon:", afternoon - morning)
print("At least one:", morning | afternoon)