import Expression as e
import Operations as o

e1 = e.Relation("T1")
e2 = e.Relation("T2")
e3 = e.Relation("T3")

j1 = o.Join(e1, e2)
j2 = o.Join(j1, e3)
print(j1)
print(j1.compute())

print(j2)
print(j2.compute())