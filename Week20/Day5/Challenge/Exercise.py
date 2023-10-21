# Instructions
# Part 1 : Quizz :
# Answer the following questions

# What is a class?
# Class is a blueprint for the creation of objects
# What is an instance?
# an instance is the creation of an object based on a blueprint (class)
# What is encapsulation?
# encapsulation is the bundling together in a blueprint (class) of both the data and the methods for handling the
# data
# What is abstraction?
# abstraction is giving access to the necessary functionality without giving access or information regarding the way
# the functionality was achieved
# What is inheritance?
# inheritance is the ability to create a blueprint based on another blueprint - extending a class with another
# class
# What is multiple inheritance?
# Multiple inheritance is the ability to create a blueprint using more than one blueprint as the source and basis
# creating a class based on several classes
# What is polymorphism?
# Polymorphism is having methods in different blueprints (classes) sharing the same name but delivering different
# functionality based on the blueprint (class) they are called from
# What is method resolution order or MRO?
# MRO is the order in which methods are handled when a blueprint is based on multiple inheritance.


# Part 2: Create A Deck Of Cards Class.
# The Deck of cards class should NOT inherit from a Card class.

# The requirements are as follows:

# The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
# The Deck class :
# should have a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
# should have a method called deal which deals a single card from the deck. After a card is dealt, it should be
# removed from the deck.
import random


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value


class Deck:
    def __init__(self):
        self.cards = []
        for i in ["Hearts", "Diamonds", "Clubs", "Spades"]:
            for j in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]:
                self.cards.append(Card(i, j))

    def shuffle(self):
        random.shuffle(self.cards)
        return self.cards

    def deal(self):
        card_picked = random.choice(self.cards)
        self.cards.remove(card_picked)
        return self.cards


# my_deck = Deck()
# my_deck.shuffle()
# print(len(my_deck.cards))
# my_deck.deal()
# for i in my_deck.cards:
#     print(i.suit, i.value)
# print(len(my_deck.cards))
