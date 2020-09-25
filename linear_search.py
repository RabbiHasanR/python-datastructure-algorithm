def linear_search(L,x):
    '''
    This method do linear searching from list.It has two arguments L=List and x=search item.it return list index if find search item else return -1
    '''
    if not L:
        return -1
    n=len(L)
    for i in range(n):
        if L[i]==x:
            return i
    return -1

if __name__=='__main__':
    x=int(input())
    L=[1,2,3,4,5,6]
    print(linear_search(L,x))
