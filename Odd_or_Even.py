#!/usr/bin/env python
# coding: utf-8

# In[4]:


import random

class Game:
    
    def __init__(self, cpu_num, user_selection):
        self.cpu_num = random.randint(1,6)
        self.user_selection = ["Odd", "Even"]

    def cpu_choice(self, cpu_choice):
        self.cpu_choice = random.randint(1,6)
        print("The computer's choice is",choice)
        return self.cpu_choice

    def user_choice(self, user_choice):
        while(True):
            self.user_choice = input("Odd or Even? ")
            if choice in sself.user_selection:
                print("Your choice is",choice)
                return self.user_choice
            else:
                print("You did not write your answer correctly, please try again.")            

    def round_result(self):
        self.num_rounds = 0
        self.user_lives = 10
        while num_rounds < 8 and user_lives > 0:
                user_pick = self.user_choice()
                cpu_pick = self.cpu_choice()
                if (cpu_pick % 2 == 0) and (user_pick == "Even"):
                        print (f'You have {self.user_lives + self.cpu_pick} lives left')
                        self.num_rounds += 1
                        self.user_lives = user_lives + cpu_pick
                        return self.num_rounds
                        return self.user_lives
                if (cpu_pick % 2 == 0) and (user_pick == "Odd"):
                        print (f'You have {self.user_lives - self.cpu_pick} lives left')
                        self.num_rounds += 1
                        self.user_lives = user_lives - cpu_pick
                        return self.num_rounds
                        return self.user_lives
                if (cpu_pick % 2 != 0) and (user_pick == "Even"):
                        print (f'You have {self.user_lives - self.cpu_pick} lives left')
                        self.num_rounds += 1
                        self.user_lives = user_lives - cpu_pick
                        return self.num_rounds
                        return self.user_lives
                if (cpu_pick % 2 != 0) and (user_pick == "Odd"):
                        print (f'You have {self.user_lives + self.cpu_pick} lives left')
                        self.num_rounds += 1
                        self.user_lives = user_lives + cpu_pick
                        return self.num_rounds
                        return self.user_lives


# In[ ]:




