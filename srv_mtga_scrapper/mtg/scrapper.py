import requests

from mtg.entities.card import Card
from mtg.entities.card_foreign import CardForeign

class Scrapper:
    magic_api_url = 'https://api.magicthegathering.io/v1/'

    def get_all_cards(self):
        response = requests.get(self.magic_api_url+'/cards')
        received_cards = response.json()['cards']
        list_of_cards = []
        
        for received_card in received_cards:
            print('nueva carta')
            card = Card()
            card.name = received_card['name']

            if('imageUrl' in received_card):  
                card.imge_url = received_card['imageUrl']
            
            if('foreignNames' in received_card):                
                received_card_foreign_names = received_card['foreignNames']

                for foreign_name in received_card_foreign_names:
                    card_foreign = CardForeign()

                    if foreign_name['language'] == 'Spanish':
                        card_foreign.name = foreign_name['name']
                        card_foreign.text = foreign_name['text']
                        
                        card.foreign_names.append(card)
            else:
                print("not in spanish")

            
            list_of_cards.append(card)
        print(card)