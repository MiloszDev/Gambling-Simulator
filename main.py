from games import SlotMachine

if __name__ == "__main__":
    inserted_credits = float(input('Type how much money to insert:\n|:: '))

    if inserted_credits:
        slot_machine = SlotMachine(inserted_credits)
        slot_machine.show_animation()