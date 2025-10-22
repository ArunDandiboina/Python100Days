from flask import Flask, render_template
import random

g = random.randint(0, 9)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
    
@app.route('/<int:guess>')
def high_low(guess):
    if g < guess:
        return render_template('high.html')
    elif g > guess:
        return render_template('low.html')
    elif g == guess:
        return render_template('right.html')
    else:
        return render_template('index.html')
    

if __name__ == "__main__":
    app.run(debug=True)