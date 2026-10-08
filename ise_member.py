import csv

def add_member(id, name):
    with open("records.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([id, name, "Member", "-"])
    print("Member added")
def show_member():
    with open("records.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) == 4 and row[2] == "Member":
                print(row)