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

# Input Values for the story
noun_one = input("Please write a noun: ")
noun_two = input("Please write another noun: ")
verb_past_tense = input("Please write a verb in the past tense: ")
noun_three = input("Please write one more noun: ")
verb_one = input("Please write a verb: ")
adjective_one = input("Please write an adjective: ")
colour_one = input("Please write a colour: ")




line1 = (f"Twas the night before Channukah when all through the house")
line2 = (f"not a creature was stirring, not even a {noun_one}")
line3 = (f"The Menorah was lit by the table with care")
line4 = (f"in hopes that {noun_two} would be there")
line5 = (f"The children were {verb_past_tense} all snug in their beds")
line6 = (f"while visions of {noun_three} danced in their heads")
line7 = (f"When out on the roof there arose such a {verb_one}")
line8 = (f"I {adjective_one} from my bed to see what was the matter")
line9 = (f"when what to my {colour_one} eyes should appear")
line10 = (f"but a miniature Goliath holding a souvenir")
line11 = (f"not to worry though, he was just delivering a new dreidel")
line12 = (f"The End")


print(f'{line1}\n{line2}\n{line3}\n{line4}\n{line5}\n{line6}\n{line7}\n{line8}\n{line9}\n{line10}\n{line11}\n{line12}')