class Solution {
   public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        int n = strs.size();

        std::unordered_map<std::string, std::vector<int>> sol;
        for (int i = 0; i < n; i++) {
            std::vector<int> count(26, 0);
            for (char c : strs[i]) {
                count[c - 'a'] += 1;
            }
            std::string key = "";
            for (int num : count) {
                key += std::to_string(num) + ',';
            }
            sol[key].push_back(i);
        }

        std::vector<std::vector<std::string>> res;
        for (auto& [key, indices] : sol) {
            std::vector<std::string> group;
            for (int i : indices) {
                group.push_back(strs[i]);
            }
            res.push_back(group);
        }
        return res;
        
    }
};
