#### allow us to loop through

## for follow specify var help to iterate
friends = ["Jim", "Big", "Morgo", "Samantha"]
for friends in friends:
    print(friends)### iterate through letter, letter change each time it iterate through

for index in range(len(friends)): ## print all number between 0010 not inclinding 10
    print(friends[index])

for index in range(5) or range(9):
    if index == 0:
        print("first iteration")
    else:
       print("Not first")