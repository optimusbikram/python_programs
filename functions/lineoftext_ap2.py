#with the use of dictionaries, write a function that takes a line of text as input and returns a dictionary where the keys are the words in the line and the values are the lengths of those words. The function should also handle cases where the input is empty or consists only of whitespace, and it should ignore any non-alphabetic characters.
def wordlengths(line):
  if(len(line.strip())==0):
     print("No words entered.")
     return
  elif(line.isdigit()):
        print("Input is a number, not a line of text.")
        return
  else:
      words = line.split() #splits the line into words
      d= dict()
      for word in words:
          d[word] = len(word)
      for word, length in d.items():
           print("\t{} ---> {}".format(word, length))

def main():
    line = input("Enter a line of text: ")
    wordlengths(line)


   #print("Length of each word: ",lengths)
if __name__=="__main__":    main()  