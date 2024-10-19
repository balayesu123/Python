
#Approach1
import Animal
import Bird

print(Animal.animal())
print(Animal.bird())

print(Bird.animal())
print(Bird.bird())

#output:
# Lion
# Parrot
# Tiger
# picock

#Approach2

from Animal import *

print(animal())
print(bird())

from Bird import *

print(animal())
print(bird())

#output:
# Lion
# Parrot
# Tiger
# picock

#Approach3  In this approach we will get data from latest import function

from Animal import *
from Bird import *

print(animal())
print(bird())

print(animal())
(print(bird()))

#output:
# Tiger
# picock
# Tiger
# picock