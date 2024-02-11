from flask import Flask, render_template, request, redirect, url_for, jsonify
from challenge.challenge import Challenge

# Initialize app
app = Flask(__name__)

# Initialize game
game = None

@app.route('/')
def index():
    return render_template('index.html')  # Create an index.html in templates to start a new game

# Global variable to hold the game state
@app.route('/start', methods=['GET'])
def start_game():
    global game
    game = Challenge()  # Initialize a new game instance
    game.new_game()
    return redirect(url_for('game_state'))

@app.route('/play_card', methods=['POST'])
def play_card():
    card = request.form['card']
    pile = request.form['pile']
    # Assuming you have a function to validate and play the card
    success = game.deck.play_card(int(card), pile)  # Adjust this line as necessary
    return jsonify(success=success)


@app.route('/game_state', methods=['GET'])
def game_state():
    state = game.deck.check_state_of_challenge()
    # Pass the necessary game state information to your template
    pile_values = [x.top_card for x in [game.deck.pile1, game.deck.pile2, game.deck.pile3, game.deck.pile4]]
    hand = [int(x) for x in game.deck.hand.cards]
    return render_template('game_state.html', state=state, hand=hand, pile_values=pile_values)

@app.route('/draw_cards', methods=['GET'])
def draw_cards():
    cards_drawn = game.deck.deal_cards()
    if cards_drawn:
        hand = [int(x) for x in game.deck.hand.cards]
        return jsonify(success=cards_drawn, hand=hand)
    return jsonify(success=bool(cards_drawn))


if __name__ == "__main__":
    app.run(debug=True)