class Solution:

    def twoSum(self, nums, target):
        # 寻找和为target的两个元素
        for each_1 in nums:
            for each_2 in nums:
                if int(each_1) + int(each_2) == target:
                    indexes.append(nums.index(each_1))
                    indexes.append(nums.index(each_2))
        return indexes

nums = []
indexes = []
# 创建nums列表
active = True
while active:
    num = input("请输入整数数组元素：")
    if num:
        nums.append(num)
    else:
        active = False
 # 确定target值
target = input("请输入目标值：")
target_int = int(target)
result = Solution.twoSum(nums, target_int)
print(result)
