def search (self, nums : list [int], target:int) -> int:
    N=len(nums)
    first = 0
    last= N-1

    while First<= Last:
        mid= (First+Last) // 2
        if nums[mid]== target:
            return mid
        elif nums[mid] < target:
            First = mid+1
        else:
            Last= mid-1
        return -1 
list = [0,1,2,3,4,5,6,7,8,9,10]
len=11
