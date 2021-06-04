"""
Illustration of creation of class, generation of random numbers in a given range and while loop
"""
import random


class Enemy:
    player_hp = 260

    def __init__(self, attack_low, attack_high):
        self.attack_low = attack_low
        self.attack_high = attack_high

    def get_attack(self):
        print(self.attack_low)


e = Enemy(60, 80)

enemy_attack_low = 60
enemy_attack_high = 80

while e.player_hp > 0:
    damage = random.randrange(enemy_attack_low, enemy_attack_high)
    e.player_hp = e.player_hp - damage
    if e.player_hp <= 30:
        e.player_hp = 30
    print('enemy strikes for', damage, 'points of damage. Current HP is', e.player_hp)
    if e.player_hp == 30:
        print("You have low health. You've been teleported to the nearest inn.")
        break
