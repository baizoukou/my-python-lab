### create a basic list
## how to access individual list

number_grid = [
    [2,1,4],
    [0,9,8],
    [0]
]


## nexted forloop
for row in number_grid:
    for col in row:
        print(col)##print every single val inside of the num grid
