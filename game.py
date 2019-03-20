#!/usr/bin/env python
# -*- coding: utf-8 -*-\

import random
import argparse
import re


class User(object):

    def __init__(self):
        self.name = raw_input('Enter a player name: ')
        self.player_score = 0

    def add_points(self, points):
        self.player_score += points


class Dye(object):

    # Choose how many sides your dye has
    def __init__(self, sides):
        self.sides = [i + 1 for i in range(sides)]

    def roll_dye(self):
        return random.choice(self.sides)


class PigGameInstance(object):

    def __init__(self):
        self.player_data = {}
        self.pending_points = 0
        self.current_player_turn = None
        self.player_iter = iter(self.player_data)

    def add_player(self, user):
        self.player_data[user.name] = user.player_score

    def check_if_winner(self):
        for player in self.player_data:
            if player[1] >= 100:
                print '{} has won the game! \n Would you like to play again?'.format(
                    player[0])
                return

    def display_scores(self):
        # Format the dictionary entries and join the list to the string
        print '''\n################# SCOREBOARD #################\n\n{}\n\n##############################################\n
        '''.format(' \n'.join('{} : {}'.format(key, val) for (key, val) in self.player_data.items()))

    def award_points(self, player_name):
        self.player_data[player_name] += self.pending_points

    def reset_state(self):
        self.player_data.clear()
        self.pending_points = 0

    def player_turn(self):
        # Cycle through players
        self.player_iter.next()
        # Get input and validate
        player_response = raw_input('Will you Roll or Hold?')
        if not re.match(r'(roll|hold|r|h)', player_response, flags=re.IGNORECASE):
            raise ValueError('Please enter one of the two valid responses.')
        return player_response


def main():

    # Initialize game
    pig_game = PigGameInstance()

    player_count = raw_input('Set amount of players for this game: ')
    for _ in range(int(player_count)):
        pig_game.add_player(User())

    pig_game.display_scores()


if __name__ == '__main__':
    main()
