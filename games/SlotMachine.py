import random
import os
import time

class SlotMachine:
    def __init__(self, credits: float) -> None:
        self.bet = 10
        self.potential_win = 0
        self.reels = ['7️⃣', '🔔', '🍉', '🍋', '🍒']
        self.combs = []

        self.remaining_credits = credits
        self.final_combination = [['7️⃣', '7️⃣', '7️⃣'], ['🔔', '🔔', '🔔'], ['🍉', '🍉', '🍉'], ['🍋', '🍋', '🍋'], ['🍒', '🍒', '🍒']]
    def generate_random_combination(self):
        combination = [random.choice(self.reels) for _ in range(3)]
        return combination

    def check_for_win(self):
        time.sleep(1)
        if self.final_combination in self.combs:
            print(f'You Won!')
            return True
        else:
            print(f'You lost')
            return False

    def show_animation(self):
        print("Spinning...")
        for _ in range(10):
            os.system('cls' if os.name == 'nt' else 'clear')
            combination = self.generate_random_combination()
            print(" ".join(combination))
            time.sleep(0.2)
            
        self.final_combination = self.generate_random_combination()
        os.system('cls' if os.name == 'nt' else 'clear')
        print(" ".join(self.final_combination))
        
        self.update_credits()
    def update_credits(self):
        if self.check_for_win():
            self.remaining_credits *= 10
            print(f'Remaining Credits: {self.remaining_credits}')
        else:
            self.remaining_credits -= self.bet
            print(f'Remaining Credits: {self.remaining_credits}')