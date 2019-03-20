#!/usr/bin/env python
# -*- coding: utf-8 -*-\

import random
import argparse
import re


class User(object):

    def __init__(self):
        self.name = raw_input('Enter a player name: ').strip()
        self.player_score = 0

    def add_points(self, points):
        self.player_score += points


class Dye(object):

    # Choose how many sides your dye has
    def __init__(self, sides):
        self.sides = [i + 1 for i in range(sides)]

    def roll(self):
        return random.choice(self.sides)


class PigGameInstance(object):

    def __init__(self):
        self.player_data = {}
        self.pending_points = 0
        self.current_player_turn = None

    def add_player(self, user):
        self.player_data[user.name] = user.player_score

    def check_if_winner(self):
        for key, val in self.player_data:
            if val >= 100:
                print '{} has won the game! \n Would you like to play again?'.format(
                    key)
                self.reset_state()
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

    def get_current_player(self):
        return self.current_player_turn

    def player_turn(self):
        # Get input and validate
        player_response = raw_input('Will you Roll or Hold? ').strip()
        if not re.match(r'(roll|hold|r|h)', player_response, flags=re.IGNORECASE):
            raise ValueError('Please enter one of the two valid responses.')
        return player_response


def main():

    # Initialize game
    pig_game = PigGameInstance()
    game_dye = Dye(6)

    # Set up the match
    player_count = int(
        raw_input('Set amount of players for this game: ').strip())
    for _ in range(player_count):
        pig_game.add_player(User())

    while pig_game:

        for key, val in pig_game.player_data.items():
            pig_game.current_player_turn = key
            curr_player = pig_game.get_current_player()
            bad_roll = False

            while bad_roll == False:
                response = pig_game.player_turn()
                if re.match(r'(roll|r)', response, flags=re.IGNORECASE):
                    current_roll = game_dye.roll()
                    if current_roll == 1:
                        bad_roll = True
                        continue
                    else:
                        pig_game.pending_points += current_roll
                        pig_game.player_data[curr_player] += pig_game.pending_points
                        pig_game.display_scores()
                        pig_game.check_if_winner()
                else:
                    continue


if __name__ == '__main__':
    main()
