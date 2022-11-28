# mad libs project
#EXTRA 1: Instead of specifying the sentences or story to convert, write a story in a file and read it from your program. Make sure to include the file in your repo and that your program reads it correctly.
#EXTRA 2: Add some replacements that are unique, that is, the first time you see them you select on randomly but then you keep reusing that replacement.

#first, let's establish the parts of speech and their respective lists

adjectives=["exciting", "fun", "boring", "breezy", "hot", "cold", "loud", "quiet", "peaceful", "chaotic"]
nouns=["river", "lake", "mountain", "hotel", "beach", "fire department", "ditch", "raveen", "valley"]
verbs=["hiking", "crying", "laughing", "hanggliding", "coding", "swimming", "hurling", "running"]
names=["Tommy", "Jessie", "Michael Jackson", "Drake", "Josh", "Betsy"]

#next, let's open the data file
f = open('madlibsstory.txt')
#read the file
data= f.read()
#split it into words
storyContent = data.split()

#then, create a variable for the main character's name that remains constant throughout the story.

import random

randnames= random.choice(names)
storyContent= [item.replace("<name>", randnames) for item in storyContent]

#then, replace the placeholders in the story with the randomly selected parts of speech from the lists. 
#thank you Derek for explaining how to use random.choice to ensure the parts of speech are randomized each time the code is run!

storyContent= [item.replace("<adjective>", random.choice(adjectives)) for item in storyContent]
storyContent= [item.replace("<noun>", random.choice(nouns)) for item in storyContent]
storyContent= [item.replace("<verb-ing>", random.choice(verbs)) for item in storyContent]


#finally, print the story
print(" ".join(storyContent))