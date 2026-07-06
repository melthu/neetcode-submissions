class Solution {
   public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> sol;
        for (int i = 0; i < nums.size() - 2; i++) {
            if ((i > 0) and nums[i] == nums[i - 1]) {
                continue;
            }
            int l = i + 1;
            int r = nums.size() - 1;
            int target = -nums[i]; 
            while (l < r) {
                if (nums[l] + nums[r] == target) {
                    sol.push_back({nums[i], nums[l], nums[r]}); 
                    l++;
                    r--;
                    while (l < r and nums[l] == nums[l - 1]) {
                        l++;
                    }
                } else if (nums[l] + nums[r] < target) {
                    l++;
                } else {
                    r--;
                }
            }
        }
        return sol;
    }
};
