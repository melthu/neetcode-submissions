class Solution {
   public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();

        std::unordered_map<int, int> c = {};
        for (int i = 0; i < n; i++) {
            c[target - nums[i]] = i;
        }

        for (int i = 0; i < n; i++) {
            if ((c.contains(nums[i])) and (c[nums[i]] != i)) {
                return {i, c[nums[i]]};
            }
        }
    }
};
