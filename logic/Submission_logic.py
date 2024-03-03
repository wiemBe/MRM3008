import collections, sys, os
from logic import *

############################################################

# Problem 1: propositional logic


# Gorev: "Eger mevsim yaz ise ve biz izmir'de isek yagmur yagmaz"

def problem11():

    # Bilgi tabani ve cikarim metodu

    kb=createResolutionKB()

    # Onermeleri tanimlayin

    Yaz = Atom('Yaz')               
    Izmir = Atom('Izmir')       
    Yagmur = Atom('Yagmur')                   
    
    # Gercekleri ve Kurallari bilgi tabanina ogretin

    kb.tell(And(Yaz,Izmir))
    kb.tell(Implies(And(Yaz, Izmir), Not(Yagmur)))

    print(kb.ask(Not(Yagmur)))


# Gorev: " Cimler islaktir ancak ve ancak yagmur yagiyorsa veya fiskiyeler acik ise"

def problem12():

    # Bilgi tabani ve cikarim metodu

    kb=createResolutionKB()
    
    # Onermeleri tanimlayin

    Yagmur = Atom('Yagmur')             
    Islak = Atom('Islak')                
    Fiskiye = Atom('Fiskiye') 
    
    # Gercekleri ve Kurallari bilgi tabanina ogretin

    kb.tell(Equiv(Islak, Or(Yagmur, Fiskiye)))
    kb.tell(And(Islak,Not(Fiskiye)))
    
    print(kb.ask(Yagmur))


# Gorev: " Gunduz ya da gecedir ikisi birden degildir."

def formula13():

    # Bilgi tabani ve cikarim metodu

    kb=createResolutionKB()

    # Onermeleri tanimlayin

    Gunduz = Atom('Gunduz')     
    Gece = Atom('Gece') 

    # Gercekleri ve Kurallari bilgi tabanina ogretin

    return Or(And(Gunduz, Not(Gece)), And(Not(Gunduz), Gece))

"""
############################################################
# Problem 2: first-order logic

# Sentence: "Herkesin bir annesi vardir"
def formula2a():
    
    def Kisidir(x): return Atom('Kisidir', x)        
    def Annesidir(x, y): return Atom('Annesidir', x, y)  

   
    return Forall('$x', Exists('$y', Implies(Kisidir('$x'), Annesidir('$x', '$y'))))


# Sentence: " Cocugu olmayan en az bir kisi vardir."

def formula2b():
    # Predicates to use:
    def Kisidir(x): return Atom('Kisidir', x)        
    def Cocugudur(x, y): return Atom('Cocugudur', x, y)    

   

    return Exists('$x', Not(Exists('$y', Implies(Kisidir('$x'), Cocugudur('$x', '$y')))))


# Return a formula which defines Daughter in terms of Female and Child.

# See parentChild() in examples.py for a relevant example.
def formula2c():
    # Predicates to use:
    def Female(x): return Atom('Female', x)            # whether x is female
    def Child(x, y): return Atom('Child', x, y)        # whether x has a child y
    def Daughter(x, y): return Atom('Daughter', x, y)  # whether x has a daughter y

    return Forall('$x', Forall('$y', Equiv(
            And(Child('$x', '$y'), Female('$y')),
            Daughter('$x', '$y')
        )))


# Return a formula which defines Grandmother in terms of Female and Parent.
# Note: It is ok for a person to be her own parent

def formula2d():
    # Predicates to use:
    def Female(x): return Atom('Female', x)                  # whether x is female
    def Parent(x, y): return Atom('Parent', x, y)            # whether x has a parent y
    def Grandmother(x, y): return Atom('Grandmother', x, y)  # whether x has a grandmother y

    return Forall('$x', Forall('$z', Equiv(
        And(Exists('$y', And(Parent('$x', '$y'), Parent('$y', '$z'))), Female('$z')),
        Grandmother('$x', '$z')
    )))


############################################################
# Problem 5: Tek ve cift sayilar

# Return the following 6 laws:

# 0. Each number $x$ has exactly one successor, which is not equal to $x$.
# 1. Each number is either even or odd, but not both.
# 2. The successor number of an even number is odd.
# 3. The successor number of an odd number is even.
# 4. For every number $x$, the successor of $x$ is larger than $x$.
# 5. Larger is a transitive property: if $x$ is larger than $y$ and $y$ is
#    larger than $z$, then $x$ is larger than $z$.
# Query: For each number, there exists an even number larger than it.
def ints():
    def Even(x): return Atom('Even', x)                  # whether x is even
    def Odd(x): return Atom('Odd', x)                    # whether x is odd
    def Successor(x, y): return Atom('Successor', x, y)  # whether x's successor is y
    def Larger(x, y): return Atom('Larger', x, y)        # whether x is larger than y
    
    # Note: all objects are numbers, so we don't need to define Number as an
    # explicit predicate.
    # Note: pay attention to the order of arguments of Successor and Larger.
    # Populate |formulas| with the 6 laws above and set |query| to be the
    # query.
    # Hint: You might want to use the Equals predicate, defined in logic.py.  This
    # predicate is used to assert that two objects are the same.
    formulas = []
    query = None

    formulas.append(Forall('$x', Exists('$y',
        AndList([Successor('$x', '$y'),
            Not(Equals('$x', '$y')),
            Forall('$z', Implies(Successor('$x', '$z'), Equals('$y', '$z')))])
        )))
    formulas.append(Forall('$x', Or(
        And(Even('$x'), Not(Odd('$x'))),
        And(Odd('$x'), Not(Even('$x')))
        )))
    formulas.append(Forall('$x', Forall('$y', Implies(
        And(Even('$x'), Successor('$x', '$y')),
        Odd('$y'))
        )))
    formulas.append(Forall('$x', Forall('$y', Implies(
        And(Odd('$x'), Successor('$x', '$y')),
        Even('$y'))
        )))
    formulas.append(Forall('$x', Forall('$y', Implies(
        Successor('$x', '$y'),
        Larger('$y', '$x')
        ))))
    formulas.append(Forall('$x', Forall('$y', Forall('$z',
       Implies(
            And(Larger('$x', '$y'), Larger('$y', '$z')),
            Larger('$x', '$z')
        )))))
    # END_YOUR_CODE
    query = Forall('$x', Exists('$y', And(Even('$y'), Larger('$y', '$x'))))
    return (formulas, query)
"""
