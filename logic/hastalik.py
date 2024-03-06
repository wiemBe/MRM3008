from logic import *
import sys

kb=createResolutionKB()

class hasta():
	def __init__(self,tansiyon,ates,midebulantisi,basdonmesi):
		self.tansiyon=tansiyon
		self.ates=ates
		self.midebulantisi=midebulantisi
		self.basdonmesi=basdonmesi

ahmet=Constant('ahmet')
mehmet=Constant('mehmet')
hilmi=Constant('hilmi')
mazhar=Constant('mazhar')

def Tansiyonvar(x,tansiyon):
	if (tansiyon>13):
		return Atom('Tansiyon',x)
	else:
		return Not(Atom('Tansiyon',x))
def Atesivar(x,ates):
	if (ates >37):
		return Atom('Ates',x)
	else:
		return Not(Atom('Ates',x))
def Xhastasi(x):
	return  And(Tansiyonvar(x))

