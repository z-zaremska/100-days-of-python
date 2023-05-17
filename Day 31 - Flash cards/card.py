import pandas as pd


class Card:
    def __init__(self):
        self.language_A = ''
        self.language_B = ''
        self.word_A = ''
        self.word_B = ''
        self.guessed = False

    def card_guessed(self):
        self.guessed = True


class CardManager:
    def __init__(self, from_lang_a, to_lang_b):
        self.unguessed_cards = []
        self.guessed_cards = []
        self.from_lang_A = from_lang_a.title()
        self.to_lang_B = to_lang_b.title()
        self.memorized_cards_num = 0

    def create_cards(self, list_of_words):
        """Create cards and assign to them word with its translation."""
        number_of_cards = len(list_of_words)

        for i in range(number_of_cards):
            card_set = list_of_words[i]

            new_card = Card()
            new_card.language_A = self.from_lang_A
            new_card.language_B = self.to_lang_B
            new_card.word_A = card_set[f'{self.from_lang_A}']
            new_card.word_B = card_set[f'{self.to_lang_B}']

            self.unguessed_cards.append(new_card)

    def add_card_to_guessed(self, card):
        card.card_guessed()
        if card.guessed is True:
            self.guessed_cards.append(card)
            self.unguessed_cards.remove(card)
        self.memorized_cards_num += 1

    def save_progress(self):
        words_to_learn_dict = {
            f'{self.from_lang_A}': [],
            f'{self.to_lang_B}': []
        }

        for card in self.unguessed_cards:
            words_to_learn_dict[f'{self.from_lang_A}'].append(card.word_A)
            words_to_learn_dict[f'{self.to_lang_B}'].append(card.word_B)

        words_to_learn = pd.DataFrame.from_dict(words_to_learn_dict)
        words_to_learn.to_csv('./data/words_to_learn.csv', index=False)
