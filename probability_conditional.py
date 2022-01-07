"""
Conditional probability
@date 07/01/22
@author Imran and Joel Grus
"""

import enum, random

#Enum is a typed set of enumerated values. We can use them
# to make our code more descriptive and readable.


class Kid(enum.Enum):
    BOY = 0
    GIRL = 1

def random_kid() -> Kid:
    return random.choice([Kid.BOY, Kid.GIRL])

"""
What is the probability of the event "both children are girls" (B) conditional on the
event "the older child is a girl" (G)

"""
    
both_girls = 0
older_girl = 0
either_girl = 0


random.seed(0)

for i in range(10000):
    younger = random_kid()
    older = random_kid()
    if older == Kid.GIRL:
        older_girl += 1
    if older == Kid.GIRL and younger == Kid.GIRL:
        both_girls += 1
    if older == Kid.GIRL or younger == Kid.GIRL:
        either_girl += 1

print("P(both | older):", both_girls/older_girl) # ~0.514 
print("P(both | either):", both_girls/either_girl) # ~ 0.33

