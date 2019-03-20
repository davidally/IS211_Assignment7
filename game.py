#!/usr/bin/env python
# -*- coding: utf-8 -*-\

import random
import argparse


class User(object):

    def __init__(self, player_name):
        # if not isinstance(player_name, basestring):
        #     raise ValueError('Please input a proper name.')
        self.name = player_name
        self.player_score = 0

    def add_points(self, points):
        self.player_score += points


class Dye(object):

    # Choose how many sides your dye has
    def __init__(self, sides):
        self.sides = [i + 1 for i in range(sides)]

    def roll_dye(self):
        return random.choice(self.sides)


class GameInstance(object):

    def __init__(self):
        self.player_data = {}
        self.pending_points = 0
        self.current_player_turn = None

    def add_player(self, user):
        self.player_data[user.name] = user.player_score

    def get_highest_score(self):
        print max(self.player_data, key=self.player_data.get)

    def display_scores(self):
        # Format the dictionary entries and join the list to the string
        print '''\n################# SCOREBOARD #################\n\n{}\n\n##############################################\n
        '''.format(' \n'.join('{} : {}'.format(key, val) for (key, val) in self.player_data.items()))

    def award_points(self, player_name):
        self.player_data[player_name] += self.pending_points

    def reset_state(self):
        self.player_data.clear()
        self.pending_points = 0


def main():
    parser = argparse.ArgumentParser()

    start = GameInstance()

    start.add_player(User('Ronald McJenkins'))
    start.award_points('Ronald McJenkins')
    start.add_player(User('Tony Toucan'))

    start.display_scores()


if __name__ == '__main__':
    main()
