#!/usr/bin/env python
# coding: utf-8

# In[13]:


import random

class Game:

    def __init__(self):
        self.cpu_num = random.randint(1,6)
        self.user_selection = ["Odd", "Even"]

    def Cpu_choice(self):
        self.cpu_choice = random.randint(1,6)
        print("The computer's choice is",self.cpu_choice)
        return self.cpu_choice

    def User_choice(self):
        while(True):
            self.user_choice = input("Odd or Even? ")
            if self.user_choice in self.user_selection:
                print("Your choice is",self.user_choice)
                return self.user_choice
            else:
                print("You did not write your answer correctly, please try again.")

    def round_result(self, game):
        num_rounds = 0
        user_lives = 10
        while num_rounds < 8 and user_lives > 0:
                user_pick = game.User_choice()
                cpu_pick = game.Cpu_choice()
                if (cpu_pick % 2 == 0) and (user_pick == "Even"):
                        print (f'You have {user_lives + cpu_pick} lives left')
                        num_rounds += 1
                        user_lives = user_lives + cpu_pick
                if (cpu_pick % 2 == 0) and (user_pick == "Odd"):
                        print (f'You have {user_lives - cpu_pick} lives left')
                        num_rounds += 1
                        user_lives = user_lives - cpu_pick
                if (cpu_pick % 2 != 0) and (user_pick == "Even"):
                        print (f'You have {user_lives - cpu_pick} lives left')
                        num_rounds += 1
                        user_lives = user_lives - cpu_pick
                if (cpu_pick % 2 != 0) and (user_pick == "Odd"):
                        print (f'You have {user_lives + cpu_pick} lives left')
                        num_rounds += 1
                        user_lives = user_lives + cpu_pick

def main():


    Odd_or_Even = Game()

    Odd_or_Even.round_result(Odd_or_Even)


if __name__ == '__main__':
    main()
