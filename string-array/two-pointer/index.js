/* 

1

First method of using two pointers involves starting at both ends of an array or string and inching back towards eachother

*/

// Valid Palindrome

/**
 * @param {string} s
 * @return {boolean}
 */
var checkIfPalindrome = function (s) {
  let left = 0;
  let right = s.length - 1;

  while (left < right) {
    if (s[left] != s[right]) {
      return false;
    }

    left++;
    right--;
  }

  return true;
};

// Two sum (similar)

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {boolean}
 */
var checkForTarget = function (nums, target) {
  let left = 0;
  let right = nums.length - 1;

  while (left < right) {
    // curr is the current sum
    let curr = nums[left] + nums[right];
    if (curr == target) {
      return true;
    }

    if (curr > target) {
      right--;
    } else {
      left++;
    }
  }

  return false;
};

/*

2

Second method of two pointer would be in a case of two iterables or arrays, for instance they are sorted and you want to combine them, have two pointer at the start of both arrays and loop until one reaches the then then finish looping for the longer iterable

*/

// Combine two sorted arrays

/**
 * @param {number[]} arr1
 * @param {number[]} arr2
 * @return {number[]}
 */
var combine = function (arr1, arr2) {
  // ans is the answer
  let ans = [];
  let i = 0,
    j = 0;

  while (i < arr1.length && j < arr2.length) {
    if (arr1[i] < arr2[j]) {
      ans.push(arr1[i]);
      i++;
    } else {
      ans.push(arr2[j]);
      j++;
    }
  }

  while (i < arr1.length) {
    ans.push(arr1[i]);
    i++;
  }

  while (j < arr2.length) {
    ans.push(arr2[j]);
    j++;
  }

  return ans;
};

// squares of a sorted array
// sort an array before squaring them using their absolute values
// use two pointers to sort
var sortedSquares = function (nums) {
  const n = nums.length;
  const ans = new Array(n);
  let start = 0,
    end = n - 1;
  for (let i = n - 1; i >= 0; i--) {
    if (Math.abs(nums[start]) >= Math.abs(nums[end])) {
      ans[i] = nums[start] * nums[start];
      start++;
    } else {
      ans[i] = nums[end] * nums[end];
      end--;
    }
  }
  return ans;
};
