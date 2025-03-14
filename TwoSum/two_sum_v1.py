class Solution(object):
    def twoSum(self, nums, target):
        # Khởi tạo một HashMap (Dictionary) để lưu giá trị và chỉ số
        hashmap = {}
        
        # Duyệt qua mảng nums
        for i, num in enumerate(nums):
            complement = target - num  # Tính giá trị cần tìm
            
            # Kiểm tra nếu giá trị complement đã có trong hashmap chưa
            if complement in hashmap:
                return [hashmap[complement], i]  # Trả về chỉ số của phần tử complement và phần tử hiện tại
            
            # Nếu không có, thêm phần tử hiện tại vào hashmap
            hashmap[num] = i
