'''
Created on 19/04/2014

@author: cataldo
'''
def main():
    myList = [7,2,5,1,29,6,4,19,11]
    sortedList = quicksort(myList,0,len(myList)-1)
    print(sortedList)
    
if __name__ == "__main__":
    main()
