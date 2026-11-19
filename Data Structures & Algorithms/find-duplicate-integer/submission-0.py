class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # fast and slow
        phainon, fast = 0, 0
        while True:
            phainon = nums[phainon]
            fast = nums[nums[fast]]
            if phainon == fast:
                break
        
        # slow + slow
        scapegoat = 0
        while True:
            scapegoat = nums[scapegoat]
            phainon = nums[phainon]
            if scapegoat == phainon:
                return scapegoat