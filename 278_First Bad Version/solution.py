# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        high = n
        low = 0
        mid = 0
        while low <= high:
            mid = (high + low) // 2
            if isBadVersion(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low
        
