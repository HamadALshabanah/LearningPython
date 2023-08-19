def containsDuplicate( nums: list[int]) -> bool:
        hashset = set(nums)
        count = 0
        for n in nums:
            if n in hashset:
                count +=1
                if count >= 2:
                    return True
        return False
        
        
nums = [1,2,3,1]
x = containsDuplicate(nums)
print(x)
print('hELLO')

def trying():
    pass