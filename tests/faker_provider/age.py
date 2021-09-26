import random
from faker.providers import BaseProvider

class AgeProvider(BaseProvider):
    def get_age(self):
        ages = ['1:day', '2:days', '3:Days', '7:Days', '15:Days', '21:Days', '28:Days',
            '1:Month', '2:Months', '3:Months', '6:Months', '9:Months', '11:Months',
            '1:Years', '3:Years', '5:Years', '6:Years', '7:Years', '8:Years', '9:Years', '10:Years'
            , '15:Years', '20:Years', '22:Years', '24:Years', '25:Years', '27:Years', '29:Years', '30:Years']
        return random.choice(ages)