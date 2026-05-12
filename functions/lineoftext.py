#program to enter a line of text and length of each word


def wordlengths(line):
    words = line.split() #splits the line into words
    for word in words:
        print("\t{} ---> {}".format(word, len(word)))


"""
length = []

for word in words:
    length.append(len(word))


"""
def main():
    line = input("Enter a line of text: ")
    wordlengths(line)


   #print("Length of each word: ",lengths)
if __name__=="__main__":    main()  