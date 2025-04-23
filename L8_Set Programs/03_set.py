names_set=set()

names_set.update(["Alice", "Bob", "Charlie", "David", "Eve"])
print("Set after adding names:", names_set)

names_set.discard("Charlie")
names_set.add("Chris")
print("Set after modifying a name:", names_set)

names_set.discard("Alice")
names_set.discard("Eve")
print("Set after deleting two names:", names_set)
