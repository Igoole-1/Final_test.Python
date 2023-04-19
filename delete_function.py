def delete_note():
    note_id = int(input("Please enter note's id for deleting: "))
    for note in notes:
        if note['id'] == note_id:
            notes.remove(note)
            save_notes(notes)
            print("Thank you. Note deleted.")
        else:
            print("Sorry. This note cannot be found.")
            