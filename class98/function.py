def countword():
    filename=input("enter the file name: ")
    numberofword=0
    file=open(filename,"r")
    for line in file:
        word=line.split()
        numberofword=numberofword+len(word)

        
    print("number of word: " )
    print(numberofword)
countword()