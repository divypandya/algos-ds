def doeswin(n,arr,s):
    step = arr[s-1]
    sm = sum(arr)
    i = s-1
    while sum(arr)!=((-1)*sm):
        if arr[i]==0:
            return 'yes'
        if arr[i]<0:
            return 'no'
        if i+step < n:
            i = i+step
            step = arr[i]
            print(step)
        elif i-step > -1:
            arr[i]*=(-1)
            i = i-step
            step = arr[i]
            print(step)
        else:
            return 'no'
    
    return 'no'
        

arr = [4,2,0,2,3]
n = len(arr)
ans = doeswin(n,arr,4)
print(ans)