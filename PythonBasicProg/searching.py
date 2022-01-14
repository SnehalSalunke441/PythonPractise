# Lecture 68, 69
pos = -1
def search(li, n):
    '''
    i = 0
    while i<len(li):
        if li[i]== n :
            globals()['pos'] = i
            return True 
        i+=1       
    return False  
    '''
    for l in range(len(li)):
        if li[l] == n:
            globals()['pos'] = l
            return True      
    return False

def binsearch(li, n):
    l = 0
    u = len(li)-1
    while l<=u:
        mid = (l+u)//2
        if li[mid]==n:
            globals()['pos'] = mid
            return True
        else:
            if li[mid] < n:
                l = mid + 1
            else:
                u = mid - 1
    return False                         




li = [2, 3, 4, 6, 7, 8, 11, 15, 100, 140, 150, 887]
n = 887

if search(li, n):
    print("Found at position ", pos+1)
else:
    print("Element Not Found")    

      