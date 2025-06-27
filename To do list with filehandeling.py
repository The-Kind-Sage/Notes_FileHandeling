def create_file():
    your_note= str(input("Your list\n"))
    with open('note.txt','w') as newfile:
        newfile.write(your_note)

def display_file():
    with open('note.txt','r') as newfile:
        print(newfile.read())


def update_file():
    updated_note= str(input("Your New list\n"))
    with open('note.txt','a') as newfile:
        newfile.write(" "+updated_note)

while 2>1:
    
    print("*** TO-DO LIST ***\n")
    print("MENU: \n")
    print("1. Create a new List")
    print("2. Update to existing List")
    print("3. View List")
    print("4. Delete a list")
    print("5. close the program")

    choice= int(input("ENter your choice(1-4): "))
    if choice== 1:
        create_file()

    elif choice== 2:
        update_file()

    elif choice== 3:
            try:
                display_file()
            except FileNotFoundError:
                print("No list found, Create a list first ")

    elif choice== 4:
        print("Work in progress")

    elif choice== 5:
        break
    else:
        print("Please enter a valid choice")

        








