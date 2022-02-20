#first i will make a dictionary which stores the positions of the nums in values as list.
# if length of the list of a particular number is 1 it means this is the only one which cannot satisfy the conditions (nums[i] == nums[j])
# answer will be sum of all combination(taking any two) of the number which have length(of list) greater than 1:
# return sum

def comb(n):
    return (n*(n-1))//2
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        gg = {}
        for i in range(len(nums)):
            try:
                if nums[i] in gg.keys():
                    gg[nums[i]]+= "i"
                else:
                    gg[nums[i]] = "i"
            except:
                continue
        ans = 0
        for i in gg:
            if len(gg[i]) >1:
                ans+=comb(len(gg[i]))
        return ans
                
        
