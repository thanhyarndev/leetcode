class Solution(object):
    def twoSum(self, nums, target):
        # Tạo một danh sách các tuple (giá trị, chỉ số gốc)
        indexed_nums = [(num, index) for index, num in enumerate(nums)]
        
        # Sắp xếp danh sách theo giá trị của các phần tử
        indexed_nums.sort(key=lambda x: x[0])
        
        # Sử dụng hai con trỏ
        left, right = 0, len(nums) - 1
        
        while left < right:
            current_sum = indexed_nums[left][0] + indexed_nums[right][0]
            
            if current_sum == target:
                return [indexed_nums[left][1], indexed_nums[right][1]]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
