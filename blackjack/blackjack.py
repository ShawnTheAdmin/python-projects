from random import randint
from random import choice
import time

card_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
card_suits = ["Hearts", "Clubs", "Diamonds", "Spades"]


def draw_card():
    num = randint(0, len(card_values) - 1)
    card = card_values[num]
    return card


def hit_quit():
    return input("(H)it, (B)reak or (Q)uit?")


def start_countdown():
    print("Starting new game in..")
    for i in range(3, 0, -1):
        print(i)
        time.sleep(0.500)


def play_game():
    play = input(f"Hello! Ready to play Blackjack? (y/n) ")
    if play.lower() == "y":
        while True:
            player_hand = []
            for i in range(0, 2):
                player_hand.append(draw_card())
            hand_count = sum(player_hand)
            print(
                f"Starting value is {hand_count}. Cards are a {player_hand[0]} of {choice(card_suits)} and a {player_hand[1]} of {choice(card_suits)}."
            )
            challenge = hit_quit()
            while (
                challenge.lower() == "hit"
                or challenge[0].lower() == "h"
                and hand_count < 21
            ):
                player_hand.append(draw_card())
                if player_hand[-1] == 11:
                    ace_check = int(
                        input("You drew an Ace! would you like an 11 or a 1? ")
                    )
                    player_hand[-1] = ace_check
                hand_count = sum(player_hand)
                if hand_count >= 21:
                    break
                print(f"You drew a {player_hand[-1]}. Current value is {hand_count}")
                challenge = hit_quit()

            # evaluate winning condition
            if hand_count == 21:
                print(f"BLACKJACK!! You hit {hand_count}!")
                start_countdown()
            elif hand_count > 21:
                print(
                    f"You lose! You drew a {player_hand[-1]} putting your current hand value is {hand_count}"
                )
                start_countdown()
            elif challenge.lower() == "break" or challenge[0] == "b":
                print(f"Nice try! Your hand was {hand_count}!")
                start_countdown()
            else:
                print("Thanks for playing!")
                return


play_game()
