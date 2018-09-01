import random
TRAP_ARTISTS = [
    'Rick Ross',
    'Future',
    'Desiigner',
    'Young Jeezy'
]

class TrapArtist:
    def __init__(self, name):
        self._name = name
    
    # getter property
    @property  
    def name(self):
        return self._name

    # setter property
    @name.setter
    def name(self, name):
        if name not in TRAP_ARTISTS:
            raise ValueError(f'{name} is not a trap artist')
        self._name = name

    # these methods could be defined outside the class like normal functions. If we want to keep it in the class, we need to use staticmethod decorator

    # they are used as factory functions. They generate an instance of a class i.e. they generate objects

    @staticmethod
    def random_artist():
        return TrapArtist(random.choice(TRAP_ARTISTS))


rr = TrapArtist('Rick Ross')
# print(rr.name())    # without getter property
print(rr.name)

rr.name = 'Future'
print(rr.name)

ta = TrapArtist.random_artist()
print(ta.name)

# rr.name = 'Ricky Rose'
# print(rr.name)