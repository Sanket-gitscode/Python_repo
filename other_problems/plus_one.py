def plusOne(digits: list[int]) -> list[int]:
    
   num = int(''.join(map(str,digits)))
   num += 1
   
   return  list(map(int,str(num)))


def plusone_othersolution(array):
    
    for i in range(len(array) - 1, -1, -1):
        if array[i] < 9:
            array[i] += 1
            break
        else:
            array[i] = 0
    else:
        array.insert(0, 1)

    return array


given_digit = [1,2,3]
print(plusOne(given_digit))
print(plusone_othersolution(given_digit))
