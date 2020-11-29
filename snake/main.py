#!/usr/bin/env python
import pprint
from snake import game
from snake import snake
from snake import apple
import random
def main():
    game_object = game.Game(10,20)
    while True:
        game_object.render()
        game_input = random.choice(['w','s','a','d'])
        game_object.parse_input(game_input)
