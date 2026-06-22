class Solution {
   public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }

        std::vector<int> a(26);
        std::vector<int> b(26);

        for (int i = 0; i < s.size(); i++) {
            a[static_cast<int>(s[i]) % 26] += 1;
            b[static_cast<int>(t[i]) % 26] += 1;
        }

        return a == b;
    }
};
