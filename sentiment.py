import cohere
from flask import Flask, request, jsonify
import re

app = Flask(__name__)
cohere_client = cohere.Client('your_cohere_api_key')

# Define the sentiment examples
examples = [
    # Positive sentiment
    {'text': 'Lionel Messi played exceptionally well today!', 'label': 'positive'},
    {'text': 'Cristiano Ronaldo is the best player in the world.', 'label': 'positive'},
    {'text': 'Mbappe\'s performance was outstanding!', 'label': 'positive'},
    {'text': 'Neymar\'s skills are unparalleled.', 'label': 'positive'},
    {'text': 'Lewandowski scored a fantastic goal!', 'label': 'positive'},
    {'text': 'Benzema was incredible in today\'s match.', 'label': 'positive'},
    {'text': 'Kevin De Bruyne is a genius on the field.', 'label': 'positive'},
    {'text': 'Salah\'s speed is unbelievable!', 'label': 'positive'},
    {'text': 'Manuel Neuer made some amazing saves.', 'label': 'positive'},
    {'text': 'Virgil van Dijk is a rock in defense.', 'label': 'positive'},
    {'text': 'What a game by Messi and Neymar!', 'label': 'positive'},
    {'text': 'Cristiano and Benzema are on fire!', 'label': 'positive'},
    {'text': 'Mbappe and De Bruyne were superb today.', 'label': 'positive'},
    {'text': 'Great teamwork by Salah and Mane.', 'label': 'positive'},
    {'text': 'Outstanding play from Ronaldo and Messi.', 'label': 'positive'},

    # Negative sentiment
    {'text': 'Lionel Messi had a terrible game.', 'label': 'negative'},
    {'text': 'Cristiano Ronaldo was off his game today.', 'label': 'negative'},
    {'text': 'Mbappe missed so many chances.', 'label': 'negative'},
    {'text': 'Neymar was invisible on the field.', 'label': 'negative'},
    {'text': 'Lewandowski couldn\'t find the net.', 'label': 'negative'},
    {'text': 'Benzema had a very poor performance.', 'label': 'negative'},
    {'text': 'Kevin De Bruyne made too many mistakes.', 'label': 'negative'},
    {'text': 'Salah was out of form.', 'label': 'negative'},
    {'text': 'Manuel Neuer let in some easy goals.', 'label': 'negative'},
    {'text': 'Virgil van Dijk was not at his best.', 'label': 'negative'},
    {'text': 'Messi and Neymar were disappointing today.', 'label': 'negative'},
    {'text': 'Cristiano and Benzema were nowhere to be seen.', 'label': 'negative'},
    {'text': 'Mbappe and De Bruyne had a bad day.', 'label': 'negative'},
    {'text': 'Salah and Mane didn\'t play well.', 'label': 'negative'},
    {'text': 'Poor performance from Ronaldo and Messi.', 'label': 'negative'},

    # Neutral sentiment
    {'text': 'Lionel Messi played his usual game.', 'label': 'neutral'},
    {'text': 'Cristiano Ronaldo was just okay.', 'label': 'neutral'},
    {'text': 'Mbappe had an average performance.', 'label': 'neutral'},
    {'text': 'Neymar did not stand out today.', 'label': 'neutral'},
    {'text': 'Lewandowski had a normal match.', 'label': 'neutral'},
    {'text': 'Benzema was neither good nor bad.', 'label': 'neutral'},
    {'text': 'Kevin De Bruyne played as expected.', 'label': 'neutral'},
    {'text': 'Salah was consistent with his usual form.', 'label': 'neutral'},
    {'text': 'Manuel Neuer had a standard game.', 'label': 'neutral'},
    {'text': 'Virgil van Dijk did his job as always.', 'label': 'neutral'},
    {'text': 'Messi and Neymar played decently.', 'label': 'neutral'},
    {'text': 'Cristiano and Benzema were average today.', 'label': 'neutral'},
    {'text': 'Mbappe and De Bruyne did not shine.', 'label': 'neutral'},
    {'text': 'Salah and Mane were just alright.', 'label': 'neutral'},
    {'text': 'Routine performance from Ronaldo and Messi.', 'label': 'neutral'}
]

# List of players to recognize
players_list = [
    'Lionel Messi', 'Cristiano Ronaldo', 'Mbappe', 'Neymar', 'Lewandowski', 'Benzema', 'Kevin De Bruyne', 'Salah',
    'Manuel Neuer', 'Virgil van Dijk', 'Mane', 'Rodrygo', 'Eduardo Camavinga', 'Luka Modric', 'Sergio Ramos',
    'Erling Haaland', 'Jadon Sancho', 'Mason Mount', 'Reece James', 'Marcus Rashford', 'Harry Kane', 'Phil Foden',
    'Jack Grealish', 'Bruno Fernandes', 'Declan Rice', 'Bukayo Saka', 'Raheem Sterling'
]

@app.route('/analyze', methods=['POST'])
def analyze_comments():
    comments = request.json.get('comments')

    results = []

    for comment in comments:
        # Sentiment Analysis
        response_sentiment = cohere_client.classify(
            model='large',
            inputs=[comment],
            examples=examples
        )
        sentiment_label = response_sentiment.classifications[0].prediction

        # Extract players mentioned
        mentioned_players = [player for player in players_list if player.lower() in comment.lower()]

        results.append({
            'comment': comment,
            'players': mentioned_players,
            'sentiment': sentiment_label
        })

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
