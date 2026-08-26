def plusOne(digits: list[int]) -> list[int]:
    
   num = int(''.join(map(str,digits)))
   num += 1
   
   return  list(map(int,str(num)))
    
def plusOne_othersolution(digits: list[int]) -> list[int]:
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits

        digits[i] = 0

    return [1] + digits



given_digit = [1,2,3]
print(plusOne(given_digit))
print(plusOne_othersolution(given_digit))