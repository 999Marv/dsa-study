# example 2 binary string find length of longest substr of 1's

def find_length(s):
  left, cur, ans = 0,0,0
  for right in range(len(s)):
    if s[right] == "0":
      cur += 1

    while cur > 1:
      if s[left] == "0" :
        cur -= 1
      left += 1
    
    ans = max(ans, right - left + 1)
  
  return ans

'''
  Number of subarrays method
   do usual sliding window method
   to calculate the numeber subarrays we can have an ans count
   the number of subarrays can be calculated by right - left + 1
'''

# ex 3 subarray product less than k
def numSubarrayProductLessThanK(self, nums, k) -> int:
    if k <= 1:
        return 0

    left = ans = 0
    cur = 1

    for right in range(len(nums)):
        cur *= nums[right]
        while cur >= k:
            cur //= nums[left]
            left += 1
        ans += right - left + 1

    return ans


'''
Fixed Window method

# ex: subarray is fixed length k

  - do some iteration to initialize the first window length k
  - keep iterating in another loop while keeping that size, right goes up and so does left
  -
'''

# Example 4: Given an integer array nums and an integer k, find the sum of the subarray with the largest sum whose length is k.
def sum_subarray(nums, k):
  cur = 0

  for i in range(k):
     cur += nums[i]

  
  ans = cur

  for i in range(k, len(nums)):
    cur += nums[i] - nums[i - k]

    ans = max(ans, cur)
  
  return ans
