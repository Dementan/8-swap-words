#swap words in a phrase

phrase = input("Enter a phrase(2 words): ")
words = phrase.split(" ")  #break the phrase into separate words by space
phrase_vice_versa = words[1]+" "+words[0]  #rearrange words using indexes
print(phrase_vice_versa)
