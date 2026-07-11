class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        deque<int> w;
        vector<int> res;
        int l = 0, r = 0;
        while (r < nums.size()) {
            while (!w.empty() and nums[w.front()] < nums[r]) {
                w.pop_front();
            }
            w.push_front(r);
            if (w.back() < l) {
                w.pop_back();
            }
            if (r >= k - 1) {
                res.push_back(nums[w.back()]);
                l++;
            }
            r++;
        }
        return res;
        
    }
};
