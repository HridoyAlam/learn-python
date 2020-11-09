def insertion_sort(a,n):
    for i in range(n):
        temp = a[i]
        j = i

        while(j>0 and temp < a[j-1]):
            a[j] = a[j-1]
            j = j-1
        a[j] = temp
    return a

if __name__ == '__main__':
    a = [4,5,9,1,4,0]
    print(a)
    b = insertion_sort(a,len(a))
    
    print(b)