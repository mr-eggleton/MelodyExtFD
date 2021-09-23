from __future__ import absolute_import
from FoxDot import *

@PatternMethod
def bubble_sort(self, swaps=True): #This defines the section of the code that does the 
    items = self.data
    changes = passes = 0 # This sets the changes and passes to 0 every time this section is ran.
    last = len(items) #lens is a method that returns the length of a list.
    swapped = True
    output = []
    output += items

    while swapped:
        swapped = False
        passes += 1
        if swaps == True:
            #print(items)
            output += items
        for j in range(1, last):
            if items[j - 1] > items[j]:
                items[j], items[j - 1] = items[j - 1], items[j]  # Swap
                if swaps == True:
                    #print(items)
                    output += items
                changes += 1
                swapped = True
                last = j
        if swaps == False:
            #print(items)
            output += items
        
        if changes == 0:
            print("data presorted")

    print(output)
    return self.__class__(output)
                
def main():
    print("Stretch_Beatz Bubble Sort Algorithm")
    assert P[50,25,5,20,10].bubble_sort() == P[50, 25, 5, 20, 10, 50, 25, 5, 20, 10, 25, 50, 5, 20, 10, 25, 5, 50, 20, 10, 25, 5, 20, 50, 10, 25, 5, 20, 10, 50, 25, 5, 20, 10, 50, 5, 25, 20, 10, 50, 5, 20, 25, 10, 50, 5, 20, 10, 25, 50, 5, 20, 10, 25, 50, 5, 10, 20, 25, 50, 5, 10, 20, 25, 50], "Test 1"
    assert P[50,25,5,20,10].bubble_sort(swaps=False) == P[50, 25, 5, 20, 10, 25, 5, 20, 10, 50, 5, 20, 10, 25, 50, 5, 10, 20, 25, 50, 5, 10, 20, 25, 50], "Test 2"
    assert P[5,5,5,5,5].bubble_sort(swaps=False) == P[5,5,5,5,5], "Test 3"
    print(str(P[5,5,5,5,5].bubble_sort(swaps=False)))

if __name__ == "__main__":
    main()

