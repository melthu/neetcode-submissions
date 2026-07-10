class Solution {
   public:
    int lengthOfLongestSubstring(string s) {
        std::unordered_map<char, int> seen;
        int sol = 0;
        int l = 0, r = 0;
        while (r < s.size()) {
            if (seen.contains(s[r])) {
                l = max(l, seen[s[r]] + 1);
            }
            seen[s[r]] = r;
            sol = max(sol, r - l + 1);
            r++;
        } return sol;
    }
};
