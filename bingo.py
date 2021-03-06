from flask import Flask, render_template
import random

app = Flask(__name__)

alfa_squares = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
prez_squares = ['Abortion', 'Anthony Weiner', 'Arrested', 'Atlantic City', 'Auto industry', 'Benghazi', 'Bernie Sanders', 'Believe me', 'Bill Clinton ', 'Billions and billions', 'Chelsea Clinton', 'Clinton Foundation', 'CNN', 'Coughing', 'Crooked', 'Deplorable', 'Disaster', 'Emails', 'Guns', 'Generals', 'Huge', 'Huma Abedin', 'ISIS', 'Israel', 'Iraq War', 'Law and order', 'Lewinsky', 'Liberal', 'Libya', 'Low energy', 'Main Street', 'Make America Great Again', 'Minnesota', 'New York', 'New Jersey', 'North Carolina', 'Obama', 'Pneumonia', 'Politically Correct', 'Radical', 'Republican', 'Refugees', 'Rubble', 'Rudy Giuliani', 'Sad', 'Stamina', 'Strong', 'Small hands', 'Stop and frisk ', 'Syria', 'Take the oil', 'Trump Foundation', 'Terrorists', 'Tired', 'Trust Me', 'Unempl- oyment', 'Wall', 'Wall Street Speeches', 'Alex Jones', 'Alt-right', 'Apprentice', 'Adultery', 'Bangladesh', 'Bankruptcy', 'Basket of deplorables', 'Bigotry', 'Black Lives Matter', 'Build a wall', 'Bush family member ', 'Casino', 'China', 'Climate change', 'Crimea', 'David Duke', 'Democrat', 'Dr. Oz', 'Evolved', 'Family leave', 'Florida', 'Football helmet', 'FOX News', 'Global warming', 'Ivanka Trump', 'Khizr Khan', 'Little man', 'Loose cannon', 'Mar-a-Lago', 'Melania Trump', 'Mexico', 'Nasty tweets', 'North Korea', 'Nuclear', 'Pam Bondi', 'Press conference', 'Reckless', 'Roger Ailes', 'Roger Stone', 'Russia', 'Steaks', 'Taj Mahal', 'Tax returns', 'Temperament', 'Thin-skinned', 'Ted Cruz', 'The Polls', 'Tim Tebow', 'Totally unqualified', 'Trump Foundation', 'Trump University', 'Ukraine', 'Unfit', 'Unprepared', 'Values', 'Vladimir Putin', 'White nationalism']

def make_card(squares):

    card = []
    random.shuffle(squares)

    for i in range(24):
        card.append(squares[i])

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

@app.route("/alfa/<int:no_cards>")
def bingo(no_cards):
    bingo_cards = []
    while len(bingo_cards) < no_cards:
        bingo_cards.append(unique_card(make_card(alfa_squares), bingo_cards))
    return render_template("alfa.html", cards=bingo_cards)

@app.route("/prez/<int:no_cards>")
def prez_bingo(no_cards):
    bingo_cards = []
    while len(bingo_cards) < no_cards:
        bingo_cards.append(unique_card(make_card(prez_squares), bingo_cards))
    return render_template("prez.html", cards=bingo_cards)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
