
def demo():
    # append()
    print("\nPractice append():")
    mylist = ['ISU', 'UI', 'UNI']
    print(mylist)
    mylist.append('Drake')
    print(mylist)

    # clear()
    print("\nPractice clear():")
    mylist = ['green', 'yellow', 'red']
    print(mylist)
    mylist.clear()
    print(mylist)

    # copy() 
    print("\nPractice copy():")
    mylist = ['green', 'yellow', 'red']
    print(mylist)
    newlist = mylist.copy()
    print(newlist)

    # count() 
    print("\nPractice count():")
    mylist = ['green', 'yellow', 'red', 'green']
    print(mylist)
    x = mylist.count('green')
    print("green appears", x, "times")

    # extend()
    print("\nPractice extend():")
    mylist = ['ISU', 'UI', 'UNI']
    print(mylist)
    biglist = ['Drake', 'DMACC', 'Simpson']
    mylist.extend(biglist)
    print(mylist)

    # index()
    print("\nPractice index():")
    mylist = ['ISU', 'UI', 'UNI']
    print(mylist)   
    x = mylist.index('ISU')
    y = mylist.index('UI')
    z = mylist.index('UNI')
    print(x ,y , z)

    # insert()
    print("\nPractice insert():")
    mylist = ['ISU', 'UI', 'UNI']
    print(mylist)
    mylist.insert(2, 'Drake')
    print(mylist)

    # pop()
    print("\nPractice pop():")
    mylist = ['ISU', 'UI', 'UNI', 'Drake']
    print(mylist)
    mylist.pop(2)
    print(mylist)

    # remove()
    print("\nPractice remove():")
    mylist = ['ISU', 'UI', 'UNI', 'Drake']
    print(mylist)
    mylist.remove('UNI')
    print(mylist)

    # reverse()
    print("\nPractice reverse():")
    mylist = ['ISU', 'UI', 'UNI', 'Drake']
    print(mylist)
    mylist.reverse()
    print(mylist)

    # sort()
    print("\nPractice sort():")
    mylist = [1, 5,87,23,53,1,2,3,6,3,34]
    print(mylist)
    mylist.sort()
    print(mylist)

    
    

demo()