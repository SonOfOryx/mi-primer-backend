from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Word list for the game
WORD_LIST = ["python", "flask", "hangman", "coding", "developer"]

# Game data
game_state = {
    "word": "python",
    "guesses": [],
    "max_attempts": 6
}

def reset_game():
    """Reset the game state with a new word."""
    game_state["word"] = random.choice(WORD_LIST)
    game_state["guesses"] = []

def get_display_word():
    return " ".join([letter if letter in game_state["guesses"] else "_" for letter in game_state["word"]])

def check_game_status():
    if "_" not in get_display_word():
        return "win"
    elif len(game_state["guesses"]) > game_state["max_attempts"]:
        return "lose"
    return "ongoing"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/guess', methods=['POST'])
def guess():
    letter = request.json.get("letter")
    if letter and letter not in game_state["guesses"]:
        game_state["guesses"].append(letter)
    return jsonify({
        "display_word": get_display_word(),
        "game_status": check_game_status(),
        "remaining_attempts": game_state["max_attempts"] - len(game_state["guesses"])
    })

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/gallery.html')
def projects():
    return render_template('gallery.html')

@app.route('/3D.html')
def Vr():
    return render_template('3D.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/HangMan.html')
def HangMan():
    return render_template('HangMan.html')

@app.route('/presentación.html')
def Presentations():
    return render_template('presentación.html')

@app.route('/index.html')
def IMS():
    return render_template('index.html')

@app.route('/PrimerRepo.html')
def Primero():
    return render_template('PrimerRepo.html')

@app.route('/Python.html')
def VENV():
    return render_template('Python.html')

@app.route('/Flutter.html')
def Flutter():
    return render_template('Flutter.html')

@app.route('/MODEVA.html')
def MODEVA():
    return render_template('MODEVA.html')

@app.route('/TeachableMachine.html')
def TM():
    return render_template('TeachableMachine.html')

@app.route('/TF.html')
def TF():
    return render_template('TF.html')

@app.route('/primera.html')
def primera():
    return render_template('primera.html')

@app.route('/primer_repo.html')
def repo():
    return render_template('primer_repo.html')

if __name__ == '__main__':
    app.run(port=8000,debug=True)