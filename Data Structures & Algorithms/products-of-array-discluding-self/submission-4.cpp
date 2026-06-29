class Solution {
   public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();

        std::vector<int> l(n, 1);
        std::vector<int> r(n, 1);

        for (int i = 1; i < n; i++) {
            l[i] = l[i - 1] * nums[i - 1];
        }

        for (int i = 2; i <= n; i++) {
            r[n - i] = r[n - i + 1] * nums[n - i + 1];
        }

        std::vector<int> sol(n, 1);
        for (int i = 0; i < n; i++) {
            sol[i] = l[i] * r[i];
        }

        return sol;
    }
};
