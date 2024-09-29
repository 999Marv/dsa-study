/*

Similar to two pointer
Works with ordered elements
usully works on subarray

sliding window problems can sound like:

- Find the longest subarray with a sum less than or equal to k
- Find the longest substring that has at most one "0"
- Find the number of subarrays that have a product less than k

The idea behind a sliding window is to consider only valid subarrays.

we move left (shrink) our window when the constraint is invalid and we move right because it is still valid

pseudo slding window:

function fn(arr):
    left = 0
    for (int right = 0; right < arr.length; right++):
        Do some logic to "add" element at arr[right] to window

        while WINDOW_IS_INVALID:
            Do some logic to "remove" element at arr[left] from window
            left++

        Do some logic to update the answer


**** sliding window algorithms run in O(n), which is much faster.
*/

// Example 1 length of longest sub array, sum is less than or equal to k
const findMaxSubarray = (nums, k) => {
  let left = 0;
  let cur = 0;
  let answer = 0;

  for (let right = 0; right < nums.length; right++) {
    cur += nums[right];

    while (cur > k) {
      cur -= nums[left];
      left++;
    }

    // right - length + 1 is the length of the current subarray
    answer = Math.max(answer, right - left + 1);
  }

  return answer;
};
