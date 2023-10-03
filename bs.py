def binary_search(list,first,last,x,tries=0):
    if last >= first:
        tries+=1
        guess = (first + last) // 2

        if list[guess] == x:
            return list[guess], tries

        elif list[guess] > x:
            return binary_search(list,first,guess -1,x,tries)
        else:
            return binary_search(list,guess + 1,last,x,tries)
    
    return None


arr = [ 2, 3, 4, 10, 40 ]
x = 10

result = print(binary_search(arr, 0, len(arr)-1, x))