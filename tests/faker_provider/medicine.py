import random
from faker.providers import BaseProvider

class TypeProvider(BaseProvider):
    def get_type_prefix(self):
        types = ['Tab. ', 'Iv. ', 'Cap. ', 'Syp. ', 'Inj. ']
        return random.choice(types)