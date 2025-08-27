from flask import Flask, render_template, request, jsonify, session
import random
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this in production

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_game', methods=['POST'])
def start_game():
    data = request.get_json()
    difficulty = data.get('difficulty', 'easy')
    
    # Set attempts based on difficulty
    if difficulty == 'easy':
        attempts = 10
    elif difficulty == 'hard':
        attempts = 5
    else:
        attempts = 7  # medium
    
    # Generate random number
    target_number = random.randint(1, 100)
    
    # Store game state in session
    session['target_number'] = target_number
    session['attempts_left'] = attempts
    session['game_over'] = False
    session['won'] = False
    
    return jsonify({
        'message': f'Game started! You have {attempts} attempts to guess a number between 1 and 100.',
        'attempts_left': attempts,
        'game_over': False
    })

@app.route('/make_guess', methods=['POST'])
def make_guess():
    data = request.get_json()
    user_guess = data.get('guess')
    
    # Get game state from session
    target_number = session.get('target_number')
    attempts_left = session.get('attempts_left')
    game_over = session.get('game_over')
    
    if game_over:
        return jsonify({'error': 'Game is already over. Start a new game!'})
    
    try:
        user_guess = int(user_guess)
        if user_guess < 1 or user_guess > 100:
            return jsonify({'error': 'Please enter a number between 1 and 100!'})
    except ValueError:
        return jsonify({'error': 'Please enter a valid number!'})
    
    # Compare guess
    if user_guess > target_number:
        result = 'Too high! 👍'
    elif user_guess < target_number:
        result = 'Too low! 👎'
    else:
        result = f'You got it! 🤘 The answer was {target_number} 🚀'
        session['game_over'] = True
        session['won'] = True
        return jsonify({
            'result': result,
            'attempts_left': attempts_left,
            'game_over': True,
            'won': True
        })
    
    # Decrease attempts
    attempts_left -= 1
    session['attempts_left'] = attempts_left
    
    if attempts_left == 0:
        session['game_over'] = True
        return jsonify({
            'result': f'{result}\nYou\'ve run out of guesses, you lose. 😭 The number was {target_number}',
            'attempts_left': 0,
            'game_over': True,
            'won': False
        })
    
    return jsonify({
        'result': f'{result}\nGuess again! 🙈',
        'attempts_left': attempts_left,
        'game_over': False
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
