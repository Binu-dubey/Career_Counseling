import requests

TRIVIA_API_URL = "https://opentdb.com/api.php"

def fetch_questions(amount, category, difficulty="easy", type="multiple"):
    """Fetches questions from the Open TriviaDB API."""
    params = {
        "amount": amount,
        "category": category,  # Different categories for different tests (to be chosen)
        "difficulty": difficulty,
        "type": type
    }
    response = requests.get(TRIVIA_API_URL, params=params)
    if response.status_code == 200:
        return response.json().get('results', [])
    else:
        return []
