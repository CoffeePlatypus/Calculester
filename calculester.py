import re
from random import randint
from datetime import datetime
from datetime import timedelta

class Calculester:

    # Inits cal with moods and friends
    def __init__(self):
        print('cal is awake')
        self.moods = ['happy', 'sad', 'low battery', 'horny', 'grumpy', 'silly', '101101010', 'big dick mood', 'metalic', 'playful', 'off', 'on', 'sentient']
        self.friends = ['bitch', 'cocksucker', '90% mtn dew', 'THE ginger', 'kaisa', 'village idiot', 'dm', 'Montana', 'nard', 'pussy', 'everyone']

    # Picks a random person from the list
    def pick_friend(self):
        index = randint(0, len(self.friends))
        return self.friends[index]

    # Picks a random mood
    def pick_mood(self):
        index = randint(0, len(self.moods))
        return self.moods[index]

    def street_side_to_park_on(self):
        date = datetime.today() + timedelta(days=1)
        if date.day % 2 :
            return 'Other side (odd)'
        return 'My side (even)'

    # A spaghetti list of random message logic
    def parse_message(self, message):
        text = message.content
        if message.author.id == 461263723554668550:
            return f'poop on mollie'
        elif re.search('shit', text, re.IGNORECASE):
            return '💩'
        elif re.search('cat', text, re.IGNORECASE):
            return '😸'
        elif re.search('hi', text, re.IGNORECASE):
            return f'Hi {message.author.name} :)'
        elif re.search('mood', text, re.IGNORECASE):
            return f'{self.pick_mood()}'
        else:
            return ''
        


        

        