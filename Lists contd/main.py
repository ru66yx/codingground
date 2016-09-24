# Apply to each
''' 
Takes as inputs a list and a function
mutates the list with the function
'''    
def applyToEach(L,f):
    for i in range (len(L)):
        L[i] = f(L[i])
        
def applyFuns(L,x):
    for f in L:
        print(f(x))
