list=[]
tuple=('a','b','c','d')
dictionary={'a':1,'b':2,'c':3,'d':4}
def assigningElementsList():
    n=int(input("how many values do you want to add in the list"))
    for i in range (n):
        list.append(input("enter the value"))
    print(list)
    
    
def accessingElementsTuple():
    n=int(input("enter the index of the tuple to be accessed"))
    print(tuple[n])
    
def deletingDictionaryElement():
    n=input("enter the key of the dictionary to be deleted")
    del(dictionary[n])
    print(dictionary)
        
def main():
    print("enter 1 for assigning the elements of list ")
    print("enter 2 for accessing Elements of Tuple ")
    print("enter 3 for deleting Dictionary Element ")
    c=int(input())
    if c==1:
        assigningElementsList()
    if c==2:
        accessingElementsTuple()
    if c==3:
        deletingDictionaryElement()
    
if __name__=="__main__":
    main()
