
def main():

    word = input("Input: ")
    
    twitter = ''
    vowels = 'aeiou'

    for i in word:
        if i not in vowels:
            twitter += i

    print(twitter)

main()