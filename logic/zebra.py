from logic import *

sari=Constant('sari')
mavi=Constant('mavi')
kirmizi=Constant('kirmizi')
beyaz=Constant('beyaz')
yesil=Constant('yesil')

norvec=Constant('norvec')
italya=Constant('italya')
ingiltere=Constant('ingiltere')
ispanya=Constant('ispanya')
japonya=Constant('japonya')

su=Constant('su')
cay=Constant('cay')
sut=Constant('sut')
meyvesuyu=Constant('meyvesuyu')
kahve=Constant('kahve')

diplomat=Constant('diplomat')
fizikci=Constant('fizikci')
fotografci=Constant('fotografci')
kemanci=Constant('kemanci')
boyaci=Constant('boyaci')

tilki=Constant('tilki')
at=Constant('at')
salyangoz=Constant('salyangoz')
kopek=Constant('kopek')
zebra=Constant('zebra')

def Ev(e1,e2,e3,e4,e5):
	return Atom('Ev',e1,e2,e3,e4,e5)

def Evler(e1,e2,e3,e4,e5):
	return Atom('Evler',e1,e2,e3,e4,e5)

def Ilkev(x):
	return Exists(x, And(Evler(x,'$y','$z','$t','$m')))

def Var(x):
	return Forall(x,Or(Or(Or((Or(Evler(x,'$y','$z','$t','$m'),Evler('$y',x,'$z','$t','$m')),Evler('$y','$z',x,'$t','$m')),Evler('$y','$z','$t',x,'$m')),Evler('$y','$z','$t','$m',x))))

kb=createResolutionKB()

#kb.tell(Var(Ev(kirmizi,ingiltere,'$x1','$y1','$z1')))

#kb.tell(Evler(Ev(kirmizi,ingiltere,'$x1','$y1','$z1'),Ev('$x2',italya,))



