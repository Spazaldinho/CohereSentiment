
# Sentiment Analysis Bot for Social Media Comments

This bot analyzes social media comments about soccer players, identifying the players mentioned and the sentiment of each comment.

## How to Use

### Prerequisites

- Python 3.6 or higher
- Cohere API key
- Flask

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/spazaldinho/CohereSentiment.git
    cd CohereSentiment
    ```

2. Install the required packages:

    ```bash
    pip install cohere flask
    ```

3. Set up your Cohere API key:

    Open the script (`app.py`) and replace `'your_cohere_api_key'` with your actual Cohere API key.

### Running the Bot

1. Start the Flask server:

    ```bash
    python app.py
    ```

2. Send a POST request to `http://127.0.0.1:5000/analyze` with a JSON body containing the comments to analyze:

    Example:

    ```json
    {
      "comments": [
        "Lionel Messi played exceptionally well today!",
        "Cristiano Ronaldo was off his game today.",
        "What a game by Messi and Neymar!",
        "Benzema had a very poor performance.",
        "Salah's speed is unbelievable!"
      ]
    }
    ```

3. Receive a JSON response with the players mentioned and the sentiment for each comment:

    Example:

    ```json
    [
      {
        "comment": "Lionel Messi played exceptionally well today!",
        "players": ["Lionel Messi"],
        "sentiment": "positive"
      },
      {
        "comment": "Cristiano Ronaldo was off his game today.",
        "players": ["Cristiano Ronaldo"],
        "sentiment": "negative"
      },
      {
        "comment": "What a game by Messi and Neymar!",
        "players": ["Lionel Messi", "Neymar"],
        "sentiment": "positive"
      },
      {
        "comment": "Benzema had a very poor performance.",
        "players": ["Benzema"],
        "sentiment": "negative"
      },
      {
        "comment": "Salah's speed is unbelievable!",
        "players": ["Salah"],
        "sentiment": "positive"
      }
    ]
