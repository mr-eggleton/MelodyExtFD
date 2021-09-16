
def bubble_sort(items, swaps=True): #This defines the section of the code that does the 
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
                if swaps == False:
                    #print(items)
                    output += items
                changes += 1
                swapped = True
                last = j
        if changes == 0:
            print("data presorted")
    return output
                



def main():
    print("Stretch_Beatz Bubble Sort Algorithm")
    print ("Test 1",  bubble_sort([50,25,5,20,10]))
    print ("Test 2", bubble_sort([50,25,5,20,10], swaps=False))
    print ("Test 3", bubble_sort([5,5,5,5,5], swaps=False))

if __name__ == "__main__":
    main()

