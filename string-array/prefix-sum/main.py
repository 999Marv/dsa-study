'''
Pre fix sums

Given an array nums,

prefix = [nums[0]]
for (int i = 1; i < nums.length; i++)
    prefix.append(nums[i] + prefix[prefix.length - 1])

ex = [5, 2, 1, 6, 3, 8]    prefix = [5, 7, 8, 14, 17, 25]

prefix sum can be found with prefix[j] - prefix[i - 1], or prefix[j] - prefix[i] + nums[i]


- great for finding prefix sum values in an array in o(1) time
- Building a prefix sum array is a form of pre processing

## keywords:
              sum of subarray

'''

# ex 1: Subarray Sum Query with Limit
def query_sum(nums, queries, limit):
  prefix = [nums[0]]
  for i in range(1, len(nums)):
      prefix.append(nums[i] + prefix[-1])
  
  ans = []
  for x, y in queries:
      curr = prefix[y] - prefix[x] + nums[x]
      ans.append(curr < limit)

  return ans


  
