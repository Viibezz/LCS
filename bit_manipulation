=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
~=~=~ 136 ~ Single Number ~=~=~=
=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~

XOR: 
- XORing values in any order does not affect the output
- XORing **SAME** numbers outputs [ 0 ] 
- XORing **DIFFERENT** numbers outputs [ 1 ]
    - 0 ^ 0 = 0
    - 1 ^ 1 = 0
    - 0 ^ 1 = 1
- XORing with [ 0 ] does not change the result
    - n ^ 0 = n
    - 1 ^ 0 = 1
    - 0 ^ 0 = 0
    
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.
Input: nums = [4,1,2,1,2]
Output: 4
    
######################################
Get the binary representation of each 
input value then XOR the input values 
all together and the result will be 
the single value.
######################################

[ 4,  ... 1 0 0
  1,  ... 0 0 1
  2,  ... 0 1 0
  1,  ... 0 0 1
  2   ... 0 1 0
]

if we XOR index 2 [ 0 1 0 ] with
          index 4 [ 0 1 0 ] then the output will be 
          [ 0 0 0 ] because they're the same and they cancel out.
          
if we XOR index 1 [ 0 0 1 ] with
          index 3 [ 0 0 1 ] then the output will be 
          [ 0 0 0 ] because they're the same and they cancel out.
          
We're left with index 4 [ 1 0 0 ] as the answer. 


def singleNumber(self, nums):
    o = 0
    for n in nums:
        o ^= n
    return o
