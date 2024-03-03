from logic import *


## Propositional Logic 

#Yagmur = Atom("Yagmur")
#Bisiklet = Atom("Disiklet")
#Basketbol = Atom("Basketbol")



#kb.tell(Implies(Not(Yagmur),Bisiklet))
#kb.tell(Or(Bisiklet, Basketbol))
#kb.tell(Not(And(Bisiklet, Basketbol)))
#kb.tell(Basketbol)

#print(kb.ask(Basketbol))

#kb = createResolutionKB()

## FOL
"""
ali = Constant('ali')
veli = Constant ('veli')
ahmet = Constant('ahmet')
zeynep = Constant ('zeynep')

x = Variable('$x')
y = Variable('$y')
z = Variable('$z')


def Parent(x,y): return Atom('Parent',x,y)
def Child(x,y): return Atom('Child',x,y)

def parentChild(x,y): return Forall(x, Forall(y, Equiv(Parent(x, y), Child(y, x))))
def notParent(x,y): return Forall(x, Forall(y,Implies(Parent(x,y),Not(Child(x,y)))))

kb = createModelCheckingKB()

#kb.tell(parentChild(x,y))
#kb.tell(notParent(x,y))
#kb.tell(Parent(ali,veli))

#print(kb.ask(Dad(ali))) 
"""

###TellTruth?

def TellTruth(x): return Atom('TellTruth', x)
def CrashedServer(x): return Atom('CrashedServer', x)
john = Constant('john')
susan = Constant('susan')
nicole = Constant('nicole')
mark = Constant('mark')

kb = createModelCheckingKB()
   
kb.tell(Equiv(TellTruth(john), Not(CrashedServer(john))))
kb.tell(Equiv(TellTruth(susan), CrashedServer(nicole)))
kb.tell(Equiv(TellTruth(mark), CrashedServer(susan)))
kb.tell(Equiv(TellTruth(nicole), Not(CrashedServer(nicole))))

kb.tell(Exists('$x', And(TellTruth('$x'), Forall('$y', Implies(TellTruth('$y'), Equals('$x', '$y'))))))
kb.tell(Exists('$x', And(CrashedServer('$x'), Forall('$y', Implies(CrashedServer('$y'), Equals('$x', '$y'))))))

sorgu1 = CrashedServer('$x')
sorgu2 = TellTruth('$x')

print(kb.ask(TellTruth(john)))

