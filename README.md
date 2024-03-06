# Blackjack Simulation
## Overview
This Python program simulates a game of Blackjack and includes an AI component that uses basic strategy to play against the dealer. The goal of the project is to provide a simple implementation of a Blackjack game and to showcase how an AI can play the game. Accuarcy is defined as the total number of games devided by the total wins. This showcases a rule based agent. The agent also keeps a count of the current deck which is returned after each game, depending on the count the agent will have various options which is yet to be implemented, because I dont know how to actually count cards.... 

## Features

Simulates multiple games of Blackjack using a standard deck of cards.
Implements basic Blackjack rules, including card values and dealer strategy.
Calculates the AI's accuracy in winning games based on basic strategy.

## Usage
Clone the repository to your local machine.
Run the BlackJack class from blackjack.py to start the game simulation.
Follow the on-screen prompts to specify the number of games to simulate.
The program will simulate the specified number of games and display the AI's accuracy in winning.
How to Play
The game follows standard Blackjack rules, where the goal is to get a hand value as close to 21 as possible without exceeding it.
The AI uses a basic strategy to determine whether to "hit" (take another card) or "stand" (keep the current hand).
The dealer also follows a basic strategy, where they must hit if their hand value is less than 17 and stand otherwise.

## In Development
Card counting system to improve accuracy. 