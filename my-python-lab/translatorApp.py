def translate(phrase): ## any vowels becom a key
       translation = ""
       for letter in phrase:
           ## check if letter is a translator and situation of lower and upper
            if letter.upper() in "AIEOUaeiou":
                if letter.islower():
                      translation = translation + "G"
                else:
                    translation = translation + "g"
            else:
                translation = translation + letter

       return translation

print(translate(input("Enter a phrase: ")))