goal = {"hi", "bye", "tata", "seeyou"}
goal.add("goodbye")
goal.remove("seeyou")
print(goal)
goal.pop()
print(goal)
goal.clear()
print(goal)

set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))
print(set1.intersection(set2))