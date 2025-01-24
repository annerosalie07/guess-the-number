from flask import Flask, request
import random
app = Flask(__name__)
secret_number = random.randint(1,100)
@app.route("/")
def index():
    return open ("guess_the_number.html").read()
@app.route("/guess")
def guess():
    global secret_number
    try:
        guess = int(request.args.get("number", ""))
        if guess < secret_number:
            return "Too low. Try again!"
        elif guess > secret_number:
            return "Too high. Try again!"
        else:
            secret_number = random.randint(1, 100)
            return f"Congratulations! You guessed the number: {guess}"
    except ValueError:
        return "Please enter a valid number."
if __name__ == "__main__":
    app.run(debug=True)