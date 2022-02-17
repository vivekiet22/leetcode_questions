class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        if n == 1:
            return 1
        count = 0
        sum = 0
        chain_len = 0
        for i in range(1,n):
            sum +=i
            chain_len+=1
            if sum >=n:
                break
        for l in range(0,chain_len):
            a = (n-l*(l+1)/2)/(l+1)
            if a == int(a):
                count+=1
        return count
            
        
        
        
        
        
        
        # using prefix sum
#         count = 0
#         prefix_sum = {0:0}
#         for i in range(1,n+1):
#             prefix_sum[i] = (prefix_sum[i-1]+i)
            
#         for ele in prefix_sum.values() :
#             if (ele-n) in prefix_sum.values():
#                 count+=1
#         return count
