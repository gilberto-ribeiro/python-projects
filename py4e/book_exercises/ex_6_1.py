word = input('Enter a word: ')

# i = 1
# while i <= len(word):
#     print(word[-i])
#     i = i + 1

for i in range(len(word)):
    print(word[-(i+1)])