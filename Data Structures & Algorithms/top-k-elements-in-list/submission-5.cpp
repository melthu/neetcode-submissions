class Solution {
   public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        std::unordered_map<int, int> counts;
        for (int num : nums) {
            counts[num] += 1;
        }

        std::unordered_map<int, std::vector<int>> freq;
        for (const auto& [i, count] : counts) {
            freq[count].push_back(i);
        }

        std::vector<int> sol;
        for (int i = 0; i < nums.size(); i++) {
            for (int num : freq[nums.size() - i]) {
                sol.push_back(num);
            }
            if (sol.size() == k) {
                return sol;
            }
        }
    }
};
