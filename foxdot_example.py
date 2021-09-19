#from MelodyExtFD.lib import bubble_sort
import MelodyExtFD
#p1 >> jbass((bubble_sort.bubble_sort([5,2,5,0,1,4,5,3,2])))
p1 >> jbass(P[5,2,5,0,1,4,5,3,2].bubble_sort())

p1 >> jbass(P[5,2,5,0,1,4,5,3,2].bubble_sort(swaps=False))
