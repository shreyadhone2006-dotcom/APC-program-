import csv

def add_book(id, name):
    with open("records.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([id, name, "Book", "Available"])
    print("Book added")


def show_book():
    with open("records.csv", "r") as f:
        reader = csv.reader(f)

        for row in reader:
            if len(row) == 4 and row[2] == "Book":
                print(row)