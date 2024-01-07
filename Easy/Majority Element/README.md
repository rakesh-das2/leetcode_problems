# Problem Statement
<img width="500" alt="image" src="https://github.com/CodeWithRakesh-stack/leetcode_problems/assets/43961504/d475671b-8afa-4257-ab02-1e1664144452">

# Solution

**We need to solve this problem with Boyer- Moore Majority Voting Algorithm**
##### 
# Lets understand what is Boyer- Moore Majority Voting Algorithm

This algorithim work in a fact that target element occurs in array <= N/2 times.

**So let us check the proceeding of the algorithm.**
First, choose a candidate from the given set of elements if it is the same as the candidate element, increase the votes. Otherwise, decrease the votes if votes become 0, select another new element as the new candidate.

**Python Solution**
```
def majority_element(nums):
    candidate = None
    count = 0
    for i in range(len(nums)):
        if count == 0:
            candidate = nums[i]
            count = 1
        elif nums[i] == candidate:
            count += 1
        else:
            count -= 1

    # Check if candidate avvaible n/2 times or not
    breakpoint()
    count = nums.count(candidate)
    if len(nums)/2 <= count:
        return candidate
    else:
        return -1

```

**Java Solution**
```
class Solution {
    public int majorityElement(int[] nums) {
		int count = 0;
		int candidate = 0;
		for(int n : nums) {
			if (count == 0) {
				candidate = n;
				count =1;
			}
			else if(n == candidate) {
				count+=1;
			}
			else {
				count-=1;
			}
		}
		// Check candiate in array n/2 times or not
		int count_can = 0;
		for (int data: nums) {
			if (data == candidate) {
				count_can++;
			}
		}
		if (nums.length/2 <= count_can) {
			return candidate;
		}
		else {
			return -1;
		}
	}
}
```
