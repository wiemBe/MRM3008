from kanren import Relation, facts,run

parent = Relation()

facts(parent, ("Homer", "Bart"),("Homer", "Lisa"),("Abe",  "Homer"))

#run(1, x, parent(x, "Bart"))


#run(2, x, parent("Homer", x))
