from flask import Flask, render_template
import random

app = Flask(__name__)

possible_squares = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'

def make_card(squares):

    card = []

    this_squares = squares

    while len(card) < 24:
        print(this_squares)
        square = random.choice(this_squares)
        card.append(square)
        this_squares = this_squares.replace(square,"")

    card.insert(12,"★") #free space!
    return card

def unique_card(card, existing_cards):
    if card in existing_cards:
        unique_card(make_card)
    else:
        return card


#print(bingo_cards)
@app.route("/")
def home():
    return "You have to go to specify the number of cards you want via URL, e.g. /5 for 5 cards"

@app.route("/<int:no_cards>")
def bingo(no_cards):
    bingo_cards = []
    while len(bingo_cards) < no_cards:
        bingo_cards.append(unique_card(make_card(possible_squares), bingo_cards))
    return render_template("index.html", cards=bingo_cards)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
