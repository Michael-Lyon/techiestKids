school_books = ["Maths", "English"]
novels = ["Captain underpants"]
borrowed_books = []


# show a user the number of books he has
# allow the user add more book
# allow the user remove some books
# check for a book

menu = """Please select one of the following options:
1. View all books   2. Add more books   3. Remove a book    4. Borrow a book    5. Quit"""

while True:
    print(menu)
    choice = input("> ")
    if choice == "1":
        print("These are all the books:")
        print("School Books: ")
        for a_school_book in school_books:
            print(a_school_book)
        print("Novel Books: ")
        for a_novel in novels:
            print(a_novel)
    elif choice == "2":
        print("What book would you like to add?")
        book_choice = input("school or novel (s/n)> ")
        if book_choice == "s":
            schl_book_name = input("Enter new book name: ")
            school_books.append(schl_book_name) # this adds a new item to the list
        elif book_choice == "n":
            novel_book_name = input("Enter new book name: ")
            novels.append(novel_book_name)
    elif choice == "3":
        print("Would you like to remove a school or novel book? ")
        remv = input("(s/n)> ")
        if remv == "s":
            schl_book_name = input("Enter the name of the school book: ")
            if schl_book_name in school_books:
                index_pos = school_books.index(schl_book_name) # gets the index of a particular book
                school_books.pop(index_pos) # removes a book using it's index position
                print("The book has been removed")
            else:
                print("Sorry this book was not found")
        elif remv == "n":
            novel_book_name = input("Enter the name of the novel book: ")
            if novel_book_name in novels:
                index_pos = novels.index(novel_book_name)  # gets the index of a particular book
                novels.pop(index_pos)  # removes a book using it's index position
                print("The book has been removed")
            else:
                print("Sorry this book was not found")
    elif choice == "4":
        print("Would ypou like to borrow a school or novel book?")
        brwd_choice = input("(s/n)> ")
        if brwd_choice == "s":
            brwd_school_book_name = input("Enter book name: ")
            if brwd_school_book_name in school_books:
                index_pos = school_books.index(brwd_school_book_name)
                sbrwd_book = school_books.pop(index_pos) # the removed book from school books would be saved in the variable
                borrowed_books.append(sbrwd_book)
            else:
                print("Book does not exist")
        elif brwd_choice == "n":
            brwd_novel_book_name = input("Enter book name: ")
            if brwd_novel_book_name in novels:
                index_pos = novels.index(brwd_novel_book_name)
                nbrwd_book = novels.pop(index_pos) # the removed book from school books would be saved in the variable
                borrowed_books.append(nbrwd_book)
            else:
                print("Book does not exist")

    elif choice == "5":
        print("quitting application")
        break
    else:
        print("Invalid input")
