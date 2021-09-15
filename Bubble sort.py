def bubble_sort(items): #This defines the section of the code that does the 
    changes = passes = 0 # This sets the changes and passes to 0 every time this section is ran.
    last = len(items) #lens is a method that returns the length of a list.
    swapped = True

    while swapped:
        swapped = False
        passes += 1
        if Sort == True:
            print(items)
        for j in range(1, last):
            if items[j - 1] > items[j]:
                items[j], items[j - 1] = items[j - 1], items[j]  # Swap
                if Sort == False:
                    print(items)
                changes += 1
                swapped = True
                last = j


    print(items)
    print("Number of passes =",passes)
    print("Number of swaps =",changes)


print("Stretch_Beatz Bubble Sort Algorithm ")
"""
while True:
    print("Enter as many numbers as you want.\n You can choose between 0 and 9.\nLeave a space between each one")
    numbers = input()
    items = [int(num) for num in numbers.split() if num.isdigit()]
    if items: bubble_sort(items)
"""
Sort = True
print (bubble_sort([50,25,5,20,10]))
Sort = False
print (bubble_sort([50,25,5,20,10]))
