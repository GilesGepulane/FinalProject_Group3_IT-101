# List to store notes and deleted notes (trash bin)
notes = []
delete_history = []

# Function to check if the notes list is empty
def is_note_empty():
    if len(notes) == 0:
        return True
    return False

# Function to display the current list of notes
def display_notes():
        print("Notes:")
        for i in range(len(notes)):
            print(f"{i+1}. {notes[i]}")

# Function to display the list of deleted notes
def display_history():
        print("Deleted Note/s:")
        for i in range(len(delete_history)):
            print(f"{i+1}. {delete_history[i]}")

# Function to display the main menu for the user
def display_menu():
    print("\nMenu: \n \n1. Take a note \n2. Remove a note \n3. View notes \n4. Arrange notes \n5. Edit a note \n6. Trash Bin \n7. Exit")


while True:
    #Check if notes are empty
    if is_note_empty() == True:
        print("Your notes are empty")
    else:
        display_notes()
    display_menu()
    prompt = int(input("Choose an option (1-7): "))
    
    #Add a note
    if prompt == 1:
        to_add = input("Enter a note to add: ")
        notes.append(to_add)
        print("Note added!")
        continue

    #Remove a note
    elif prompt == 2:
        #Check if list empty
        if is_note_empty() == True:
            print("Your notes are empty, please try again.")
            continue
        else:
            display_notes()
            to_remove = int(input("Enter a note to remove:"))
        #Check if the user input is valid
            if to_remove > len(notes) or to_remove == 0:
                print("Invalid note! Please try again.")
                continue
            else:
                #Add to trash bin and then remove it from the note
                delete_history.append(notes[to_remove-1])
                del notes[to_remove-1]
                print("Note removed!")
                continue

    #View notes
    elif prompt ==3:
        if is_note_empty() == True:
            continue
        else:
            display_notes()
            proceed = input("Return to Menu? (Y/N): ")
            if proceed == "Y" or proceed == "y":
                continue
            else: 
                break

    #Arrange notes in a custom order
    elif prompt == 4:
        #Check if there are 2 or more notes in order to proceed arranging notes
        if len(notes) > 1:
            while True:
                display_notes()
                to_move = int(input("Which note should I move? "))
                #Check if user input is valid
                if to_move <= len(notes) and not to_move <=0:
                    print(f"{to_move}. {notes[to_move-1]}", end=" " )
                    where = int(input("<-----Where should i put this note? "))
                    #Check If user input is valid
                    if where <= len(notes) and not where <=0:
                        #Perform the note movement and show the new arrangement
                        new = notes[to_move-1]
                        del notes[to_move-1]
                        notes.insert(where-1, new)
                        print("Notes arranged successfully!")
                        print("New Arrangements:")
                        display_notes()
                        proceed = input("Continue? (Y/N): ")
                        if proceed == "Y" or proceed == "y":
                            continue
                        else:
                            break
                    else:
                        print("Invalid Input! Please try again.")
                        break
                else:
                    print("Invalid Note!")
                    continue
        else:
            print("You need to have 2 or more notes to arrange the notes")
            continue
    
    #Edit a note
    elif prompt == 5:
        #Check if list is empty
        if is_note_empty() == True:
            print("Your notes are empty, please try again.")
        else:
            display_notes()
            to_edit =  int(input("Note to edit: "))
            if to_edit <= len(notes) and not to_edit <=0:
                modify_note = input("Modify Note: ")
                # Replace the old note with the new one
                del notes[to_edit-1]
                notes.insert(to_edit-1, modify_note)
                continue
            else:
                print("Invalid input! Please try again.")
                continue
    #Trash Bin
    elif prompt == 6:
        display_history()
        proceed = input("Continue? (Y/N): ")
        if proceed == "Y" or proceed == "y":
            continue
        else:
            break
    #Exit
    else:
        break