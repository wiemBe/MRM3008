from logic import *

a=Constant('a')
b=Constant('b')
c=Constant('c')
d=Constant('d')
e=Constant('e')
f=Constant('f')
g=Constant('g')
h=Constant('h')

def Person(x):
	return Atom('Person',x)
def Semt(x):
	return Atom('Semt',x)
def Ikamet_eder(x,y):
	return Atom('Ikamet_eder',x,y)

kb=createResolutionKB()

kb.tell(Person(a))
kb.tell(Person(b))
kb.tell(Person(c))
kb.tell(Person(d))

kb.tell(Not(Person(e)))
kb.tell(Not(Person(f)))
kb.tell(Not(Person(g)))
kb.tell(Not(Person(d)))

def PC(): 
	return Forall('$x', Implies(Person('$x'), Not(Semt('$x'))))

def CT(): 
	return Forall('$x', Implies(Not(Person('$x')), Semt('$x')))

#kb.tell(Ikamet_eder(a,e))

kb.tell(PC())
kb.tell(CT())

print(kb.ask(Semt(e)))


