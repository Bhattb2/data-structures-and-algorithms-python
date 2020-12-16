# Binary Search
Write a function called BinarySearch which takes in 2 parameters: a sorted array and the search key. Without utilizing any of the built-in methods available to your language, return the index of the array’s element that is equal to the search key, or -1 if the element does not exist.

## Approach & Efficiency
Wrote 2 functions:

- 1 function iterates over an array until it finds the value. If it does, it returns the index, if it doesn't, it returns -1.

- The second is a recursive function with the same idea as the previous one.

## Solution
For the first fuction, loop through the array until value is found

    for i in arr:
            if i == n:
                return count
            count += 1

