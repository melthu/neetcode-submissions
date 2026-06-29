class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        std::unordered_set<int> s;
        for (int num: nums) {
            s.insert(num);
        }

        int sol = 0;
        for (int num: s) {
            if (!s.contains(num - 1)) {
                int i = 0;
                while (s.contains(num + i)) {
                    i++;
                }
                sol = max(sol, i);
            }
        }
        return sol;
    }
};
