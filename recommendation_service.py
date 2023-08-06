from flask import Flask, request
import pizza_recommender

app = Flask(__name__)

@app.route('/suggest', methods=['POST'])
def suggest_pizzas():
    data = str(request.data)
    suggestion = pizza_recommender.suggest_pizzas(data)
    return suggestion

if __name__ == '__main__':
    app.run()
