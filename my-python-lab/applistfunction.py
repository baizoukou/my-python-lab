lucky_numbers = [2, 4, 8, 1, 7, 15, 27, 25, 10]
friends = ["yacubu", "rolan", "anatol", "patrick", "jony", "bel"]
friends.extend(lucky_numbers)## take friend and value of lucky num in it
print(friends)
friends.append("toby")
friends.insert(1, "rolax")## add value at index value and all other value get push back
print(friends)
friends.remove("bel")## remove value
print(friends)
print(friends.clear())## return empty elt of list
friends = ["yacubu", "rolan", "anatol", "patrick", "jony", "bel"]
friends.pop()## pop item off of this list
print(friends)
## let figure out if a certain value is in
print(friends.index("patrick"))## if a name is  not in d list is going to throw an err
friends = ["yacubu", "yacubu", "rolan", "anatol", "patrick", "jony", "bel"]
print(friends.count("yacubu"))## tells me how many time yacubu show up in the list
friends = ["yacubu", "rolan", "anatol", "patrick", "jony", "bel"]
friends.sort()
print(friends)
lucky_numbers.sort()
print(lucky_numbers)
lucky_numbers.reverse()
print(lucky_numbers)


### use of copy
friends2 = friends.copy()
print(friends2)

## used del
friends = friends2.clear()
print(friends2)