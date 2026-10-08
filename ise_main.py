from library import book
from library import member
book.add_book(101, "Python")
book.add_book(102, "Java")
member.add_member(1, "Shreya")
member.add_member(2, "Ishita")
print("Books:")
book.show_book()
print("Members:")
member.show_member()