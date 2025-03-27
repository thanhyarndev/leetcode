#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> map;  // key: number, value: index
        
        for (int i = 0; i < nums.size(); ++i) {
            int complement = target - nums[i];
            
            // Check if the complement exists in the map
            if (map.find(complement) != map.end()) {
                return {map[complement], i};  // Return the indices of the complement and current number
            }
            
            // Store the current number and its index
            map[nums[i]] = i;
        }
        
        // If no solution (though the problem guarantees there will be one), we would return an empty vector.
        return {};
    }
};
