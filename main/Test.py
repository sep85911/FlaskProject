import sys;



# while True:
#     try:
#         print(next(it));
#     except StopIteration:
#         sys.exit();

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    for i, v in enumerate(nums):
        for j, k in enumerate(nums[i+1:]):
            if v + k == target:
                return list([i, i + j + 1]);


def twoSum_Answer(nums, target):
    dic = {}   #字典     
    for i, num in enumerate(nums):

        print(dic);
        if num in dic:                
            return [dic[num], i]            
        else:
            dic[target - num] = i


a = 2;
if a == 1:
    print("fuck you");
elif a == 2:
    print("fuck you too");

for i in range(54):#循环n次就写N 下标为0 最终不含N
    pass;

for i in [11,22,33]:#直接遍历list所有值
    print(i)

for i in enumerate([11,22,33]):#用enmuerate遍历 i是一个tuple 包含key和value 或者 赋成2个值 key和value
    print(i)

import time;
import math

def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """ 
    res = [];
    if len(l1) >= len(l2):            
        for i in l1:
            temp = l2[i] + (l1[i] or 0)
            if temp >= 10:
                res[i] = temp + 1;
            else:
                res[i] = l1[i] + l2[i];               
    else:          
        for i in l2:
            temp = l1[i] + (l2[i] or 0)
            if temp >= 10:
                res[i] = temp + 1;
            else:
                res[i] = l1[i] + l2[i];    
                
    return res;

# addTwoNumbers([2,4,3],[5,6,4]);

print("hello world again")



