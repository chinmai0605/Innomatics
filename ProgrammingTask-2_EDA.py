# 1. Defanging an IP Address

class Solution:
    def defangIPaddr(self,address: str)->str:
        return address.replace('.','[.]')
        
# 2. Find Numbers with Even Number of Digits

class Solution:
    def findNumbers(self, nums: List[int])->int:
        count = 0
        for i in nums:
            digits = 0
            temp = i
            while temp > 0:
                temp //= 10
                digits += 1
            if digits % 2 == 0:
                count += 1
        return count