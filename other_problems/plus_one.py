def plusOne(digits: list[int]) -> list[int]:
    
   num = int(''.join(map(str,digits)))
   num += 1
   
   return  list(map(int,str(num)))
    

given_digit = [1,2,3]
print(plusOne(given_digit))