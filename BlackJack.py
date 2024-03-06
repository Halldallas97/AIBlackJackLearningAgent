import random

class BlackJack():
    
    def game(self, deck, dealer_strategy='basic'):
        deck_list = list(deck.keys())
        random.shuffle(deck_list) 
        tracker = {'win': 0, 'count': 0} 
        while len(deck_list) > 30:
            players_cards = []
            dealer_cards = []
            card_value = {'value': 0, 'count':0}
            for i in range(2): 
                players_cards.append(deck_list.pop())
                dealer_cards.append(deck_list.pop())
            card_value = self.hitcards(players_cards, card_value)

            while card_value['value'] <= 16: 
                card = [deck_list.pop()]
                result = self.hitcards(card, card_value)
                card_value['value'] += result['value']
                card_value['count'] = result['count']
            dealer_value = self.hitcards(dealer_cards, {'value': 0, 'count': 0})
            while dealer_value['value'] < 17 and dealer_strategy == 'basic':
                dealer_cards.append(deck_list.pop())
                dealer_value = self.hitcards(dealer_cards, dealer_value)

            if card_value['value'] <= 21 and (card_value['value'] > dealer_value['value'] or dealer_value['value'] > 21):
                print("Card value " + str(card_value['value']) + " winner")
                tracker['win'] += 1 
                tracker['count'] += card_value['count']
            else:
                print('Loss ' + str(card_value['value']))
                tracker['win'] -= 1
                tracker['count'] += card_value['count']
            card_value['value'] = 0 
            print("\n")
        return tracker
        
    def hitcards(self, player_cards, card_value):
        v = 0 
        count = card_value['count']
        for pc in player_cards:
            if 'J' in pc or 'Q' in pc or 'K' in pc: 
                v += 10
                count -= 1 
            elif pc[1] != 'A':  
                v += int(pc[1])  
                if int(pc[1]) in [2, 3, 4, 5, 6]: 
                    count += 1   
            else:
                count -= 1
                v += 11
        return {'value': v, 'count': count}
    
    def simulateGames(self, deck): 
        accuracy = 0 
        total = 0
        t = {'win':0, 'count':0, 'game':0}
        x = int(input("number of games:"))
        for i in range(x):
            tracker = self.game(deck)
            t['count'] = tracker['count']
            t['win'] = tracker['win']
            total += tracker['win']
            t['game'] = i
            
            print(t)
        accuracy = total / x
        print("AI accuracy = " + str(accuracy) )