import BlackJack as blackjack

class Main():
    card = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 11]
    suite = ['C', 'S', 'D', 'H']
    fulldeck = {}
    
    for s in suite:
        for c in card:
            fulldeck[(s, c)] = c
    game = blackjack.BlackJack()
    game.simulateGames(fulldeck)