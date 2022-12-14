import random
from replit import clear
from art import logo

card_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def random_card(card_deck):
  """Return a random card from the deck"""
  return random.choice(card_deck)


def calculate_score(cards):
  """Take a list of cards and return the score calculated from the cards"""
  if sum(cards) == 21 and len(cards) == 2:
    return 0

  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, comp_score):
  if user_score == comp_score:
    return "Draw"
  elif comp_score == 0:
    return "Lose, opponent has a blackjack"
  elif user_score == 0:
    return "Win with a Blackjack"
  elif user_score > 21:
    return "You went over. You Lose"
  elif comp_score > 21:
    return "Opponent went over. You win"
  elif user_score > comp_score:
    return "You win"
  else:
    return "You lose"
  
def play_game():
  print(logo)
  
  user_cards = []
  comp_cards = []
  is_gameover = False

  for _ in range(2):
    user_cards.append(random_card(card_deck))
    comp_cards.append(random_card(card_deck))
  
  while not is_gameover:
    user_score = calculate_score(user_cards)
    comp_score = calculate_score(comp_cards)
    
    print(f" Your cards: {user_cards}, current score: {user_score}")
    print(f" Coumputer's first card: {comp_cards[0]}")
    
    if user_score == 0 or comp_score == 0 or user_score > 21:
      is_gameover = True
    else: 
      another_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if another_deal == 'y':
        user_cards.append(random_card(card_deck))
      else: 
        is_gameover = True
  
  while comp_score != 0 and comp_score < 17:
    comp_cards.append(random_card(card_deck))
    comp_score = calculate_score(comp_cards)
  
  print(f"Your final hand: {user_cards}, final score: {user_score}")
  print(f"Computer's final hand: {comp_cards}, final score: {comp_score}")
  print(compare(user_score, comp_score))

while input("Do you want to play a game of blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()
