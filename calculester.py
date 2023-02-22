import re
from random import randint
from datetime import datetime
from datetime import timedelta
from calcalendar import CalCalendar

class Calculester:

    # Inits cal with moods and friends
    def __init__(self, fIds):
        print('cal is awake')
        self.moods = ['happy', 'sad', 'low battery', 'horny', 'grumpy', 'silly', '101101010', 'big dick mood', 'metalic', 'playful', 'off', 'on', 'sentient', 'suc', 'world domination', 'death']
        self.friends = fIds
        self.holidays = CalCalendar().holidays

    # Picks a random person from the list
    def pick_friend(self):
        index = randint(0, len(self.friends))
        return self.friends[index]

    # Picks a random mood
    def pick_mood(self):
        index = randint(0, len(self.moods))
        return self.moods[index]

    # Tells you which side of the street to park on for odd/even parking in the winter
    def street_side_to_park_on(self):
        date = datetime.today() + timedelta(days=1)
        if date.day % 2 :
            return 'Other side (odd)'
        return 'My side (even)'

    # checks if today is special
    def check_events(self):
        today = datetime.today()
        todayString = f'{today.month}-{today.day}'
        if todayString in self.holidays:
            return self.holidays[todayString]
        return False

    def check_roomate_events(self):
        today = datetime.today()
        events = []
        if today.day == 28 :
            events.append('Pay rent')
        if today.weekday() == 2:
            events.append('Take out trash')
            d = today.isocalendar()
            if d[1] % 2 == 0:
                events.append('Take out recycling')
        
        if events != []:
            return '\n'.join(events)
        return False



    def check_timesheet(self):
        d = datetime.today().isocalendar()
        if d[2] == 5 :
            return d[1] % 2 != 0
        return False

    # A spaghetti list of random message logic
    # not used by actual bot logic
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

    
        


        

        