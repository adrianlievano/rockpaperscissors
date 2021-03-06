#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
import random

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        move = input('Rock, paper, or scissors? >')
        while move not in moves:
            move = input('Please try again. Rock, paper, or scissors?>')
            if move in moves:
                break
        return move.lower()


class ReflectPlayer(Player):
    def move(self):
        try:
            move = self.their_move
        except AttributeError:
            move = random.choice(moves)
        return move

    def learn(self, my_move, their_move):
        self.their_move = their_move


class CyclePlayer(Player):
        def move(self):
            try:
                for idx, option in enumerate(moves):
                    if (self.my_move == option):
                        try:
                            move = moves[idx + 1]
                        except IndexError:
                            move = 'rock'
            except AttributeError:
                move = random.choice(moves)
            return move

        def learn(self, my_move, their_move):
            self.my_move = my_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    score = 0

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        if (beats(move1, move2) is True):
            self.score1 = self.score1 + 1
            print("Player 1 wins!")
            print(f"Player 1: {move1}  Player 2: {move2}")
            print(f"Player_1 score:{self.score1} Player_2 score:{self.score2}"
                  "")
            print(" ")

        elif (beats(move2, move1) is True):
            self.score2 = self.score2 + 1
            print("Player 2 wins!")
            print(f"Player 1: {move1}  Player 2: {move2}")
            print(f"Player_1 score: {self.score1} Player_2 score:{self.score2}"
                  "")
            print(" ")

        else:
            print("Draw!")
            print(" ")

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self, score1, score2):
        print("Game start!")
        self.score1 = score1
        self.score2 = score2

        for round in range(5):
            print(f"Round {round}:")
            self.play_round()

        if (self.score1 > self.score2):
            print('Player 1 is the winner!')
        elif (self.score2 > self.score1):
            print('Player 2 is the winner!')
        else:
            print('The score is tied. Next point wins!')
            print(" ")
            while (self.score2 == self.score1):
                print("Sudden Death Round")
                self.play_round()

        print("Game over!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), Player())
    game.play_game(0, 0)
