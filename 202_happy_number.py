class Solution:
    def isHappy(self, n: int) -> bool:
        number = n
        seen = set()
       
        while number !=1 and number not in seen:
            seen.add(number)

            number = sumNumber(number)
        
        return True

def sumNumber(number):
    sumNumbers = 0

    for charNumber in str(number):
        sumNumbers += int(charNumber) ** 2
    return sumNumbers