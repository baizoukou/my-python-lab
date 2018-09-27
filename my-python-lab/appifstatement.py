## create bool to store

is_male = True
is_tall = False

## write a ligne with combinaition of 2
if is_male or is_tall:
     print("You are a male ") ## both are true
elif is_male and not (is_tall): ## not will negate anything in ()
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but you are tall")
else:
    print("You are not a male and not tall")


