def add_contact():
    name = input("Enter the name of contact :      ")
    number = input("Enter the phone number of contact :      ")
    email = input("Enter the email of contact :      ")
    with open("contact_book.txt","a") as file:
        file.write(f"{name},{number},{email}\n")
def view_contacts():
    try:
        contact_num = 0
        with open("contact_book.txt","r") as file:
            lines = file.readlines()
            if lines == []:
                    print("Your contact book is empty")
                    return
            for line in lines:

                contact_num = contact_num + 1
                dataset = line.split(",")
                print(f"""{contact_num}.
Name:{dataset[0].strip()}
Phone Number:{dataset[1].strip()}
Email:{dataset[2].strip()}""")
    except FileNotFoundError:
        print("Your contact book is empty or not found")
def search_contact():
    try:
        search = input("Enter the name you want to search:      ")
        with open("contact_book.txt","r") as file:
            lines = file.readlines()
            found = False
            for line in lines:
                if line.startswith(search):
                    found = True
                    result = line
            if found == False:
                print("Contact not found")
            else:
                result = result.strip().split(",")
                print(f"""Name : {result[0].strip()}
Phone number : {result[1].strip()}
Email : {result[2].strip()}""")
    except FileNotFoundError:
        print("Contact book is empty or not found")
def edit_contact():
    print("Your current contacts are")
    view_contacts()
    try:
        search = input("Enter the name you want to edit contact of:      ")
        with open("contact_book.txt","r") as file:
            lines = file.readlines()
            found = False
            matched_index = -1
            for i, line in enumerate(lines):
                if line.startswith(search):
                    found = True
                    matched_index = i
                    result = line.strip().split(",")
            if found == False:
                print("Contact not found")
            else:
                print(f"""Name : {result[0].strip()}
Phone number : {result[1].strip()}
Email : {result[2].strip()}""")
                
                edit = input("Enter the field name you want to edit:    ").strip().lower()
                if edit == "name":
                    new_name = input("Enter the new name for contact:     ")
                    result[0] = new_name
                elif edit == "phonenumber":
                    new_number = input("Enter the new contact number for contact:     ")
                    result[1] = new_number
                elif edit == "email":
                    new_email = input("Enter the new email for contact:     ")
                    result[2] = new_email
                lines[matched_index] = ",".join(result) + "\n"
                with open("contact_book.txt", "w") as file:
                    for line in lines:
                        file.write(line)
                print("Contact updated successfully.")
                view_contacts()
    except FileNotFoundError:
        print("Contact book is empty or not found")
def delete_contact():
    while True:
        while True:
            try:
                try:
                    with open("contact_book.txt","r") as file:
                        lines = file.readlines()
                        if len(lines) == 0:
                            print("There are no contacts.")
                            return
                except FileNotFoundError:
                    print("The file is not found or is empty")
                    return
                print("Your contacts are")
                view_contacts()
                line_num = int(input("Enter the line number of a conatact"))-1
            except ValueError:
                print("Please enter a valid choice")
            else:
                break
        if line_num < 0 or line_num >= len(lines):
            print("please choose valid option")
            continue
        else:
            break
    lines.pop(line_num)
    with open("contact_book.txt","w") as file:
        for i in range(len(lines)):
            each_line = lines[i]
            file.write(each_line)
    print("Now your contacts are")
    view_contacts()
def option_selection():
    while True:
        while True:
            try:
                user_choice = int(input("""
========== CONTACT BOOK ==========

1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit:
            """))
            except ValueError:
                print("Please only enter a number not any other thing")
            else:
                break
        if user_choice < 1 or user_choice > 6:
            print("Please enter a valid choice")
            continue
        else:
            break
    return user_choice
def contact_book():
    while True:
        user_choice=option_selection()
        if user_choice == 1:
            add_contact()
        elif user_choice == 2:
            view_contacts()
        elif user_choice == 3:
            search_contact()
        elif user_choice == 4:
            edit_contact()
        elif user_choice == 5:
            delete_contact()
        elif user_choice == 6:
            print("Goodbye!")
            break
contact_book()
