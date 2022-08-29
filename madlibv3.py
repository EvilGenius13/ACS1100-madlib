# This is a made up take on Twas the night before Christmas but 
# with a Channukah spin.
# I added the extra code at the top because I thought it would be fun to learn
# something else.
import sys

print(f"Hi, are you ready to start?")
answer = input("Enter yes or no: ") 
if answer == "yes": 
    print("Awesome!") 
elif answer == "no": 
    print("That's too bad, maybe another time?")
    sys.exit()
else: 
    print("Please enter yes or no.") 
#check for if statement to restart back at yes or no


noun_one = input("Please write a noun: ")
noun_two = input("Please write another noun: ")
verb_past_tense = input("Please write a verb in the past tense: ")
noun_three = input("Please write one more noun: ")
verb_one = input("Please write a verb: ")
adjective_one = input("Please write an adjective: ")
colour_one = input("Please write a colour: ")




print(f"Twas the night before Channukah when all through the house")
print(f"not a creature was stirring, not even a {noun_one}")
print(f"The Menorah was lit by the table with care")
print(f"in hopes that {noun_two} would be there")
print(f"The children were {verb_past_tense} all snug in their beds")
print(f"while visions of {noun_three} danced in their heads")
print(f"When out on the roof there arose such a {verb_one}")
print(f"I {adjective_one} from my bed to see what was the matter")
print(f"when what to my {colour_one} eyes should appear")
print(f"but a miniature Goliath holding a souvenir")
print(f"not to worry though, he was just delivering a new dreidel")
print(f"The End")

