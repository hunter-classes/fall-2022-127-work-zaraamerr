#exercise 1: Write a program that allows the user to enter a string. It then prints a table of the letters of the alphabet in alphabetical order which occur in the string together with the number of times each letter occurs. Case should be ignored. 

sentence = input("Enter a sentence: ")

sentence = sentence.lower()

alphabet = 'abcdefghijklmnopqrstuvwxyz'

letter = {}
for char in sentence:
    if char in alphabet:
        if char in letter:
            letter[char] = letter[char] + 1
        else:
            letter[char] = 1

keys = letter.keys()
for char in sorted(keys):
    print(char, letter[char])

s="""this is a string with bunch of lower case letters. There's nothing a too interesting about it other than the fact that there are a bunch of words over multiple lines and we're going to do some processing on them"""
def count_words(s):
    counts = {}
    for word in s.split():
        counts.setdefault(word,0)
        counts[word] = counts[word]+1
        
    return counts

result= count_words(s)
print (result)