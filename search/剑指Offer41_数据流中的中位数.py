class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.nums.append(num)
        for i in range(len(self.nums) - 1, -1, -1):
            if i > 0:
                if self.nums[i - 1] >= num:
                    self.nums[i] = self.nums[i - 1]
                else:
                    self.nums[i] = num
                    break
            else:
                self.nums[0] = num

    def findMedian(self):
        """
        :rtype: float
        """
        n = len(self.nums)
        if n % 2 != 0:
            return self.nums[n // 2]
        else:
            return (self.nums[n // 2 - 1] + self.nums[n // 2]) / 2



me = MedianFinder()
me.addNum(6)
me.addNum(10)
me.addNum(2)
print(me.findMedian())
print(me.nums)

