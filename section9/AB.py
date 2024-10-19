#Approach1:
import A
import B

aobj=A.Animal()
aobj.display()
bobj=B.Bird()
bobj.display()

#Approach2:
from A import Animal
from B import Bird

aobj=Animal()
aobj.display()
bobj=Bird()
bobj.display()