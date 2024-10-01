import random

class SlotMachine:
    def __init__(self, credits: float) -> None:
        self.bet = 0
        self.potential_win = 0

        self.reels = ['7️⃣', '🔔', '🍉', '🍋', '🍒']

        self.remaining_credits = credits

    def generate_random_combination(self):
        for i in range(3):
            rand_choice = random.choice(self.reels)
            print(rand_choice)

    def check_for_win(self):
        pass