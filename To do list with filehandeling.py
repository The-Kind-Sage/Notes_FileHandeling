def create_file():
    your_note= str(input("Your list\n"))
    with open('note.txt','w') as newfile:
        newfile.write(your_note)

while 2>1:
    
    print("*** TO-DO LIST ***\n")
    print("MENU: \n")
    print("1. Create a new List")
    print("2. Update a existing List")
    print("3. Delete a list")
    print("4. close the program")

    choice= int(input("ENter your choice(1-4): "))
    if choice== 1:
        create_file()
    elif choice== 2:
        create_file()
    elif choice== 3:
        print("Work in progress")
    elif choice== 4:
        break
    else:
        print("Please enter a valid choice")

        








