import random

R_EATING = "I'don't like eating beacuse I'm a bot."
R_ADVICE = "IF I were you, I would use a search engine."


def unknown():
    response = ["could you please re phrase that?",
                '...',
                'Sounds about right.',
                'What does that mean?'][
        random.randrange(4)]
    return response

