"""Front Back"""
word = input("What's your word?")
midVar = word[1:len(word)-1]
print(word[len(word)-1] + midVar + word[0])
