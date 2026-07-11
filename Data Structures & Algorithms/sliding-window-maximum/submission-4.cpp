class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        deque<int> w;
        vector<int> res;
        int l = 0, r = 0;
        while (r < nums.size()) {
            while (!w.empty() and nums[w.back()] < nums[r]) {
                w.pop_back();
            }
            w.push_back(r);
            if (w.front() < l) {
                w.pop_front();
            }
            if (r >= k - 1) {
                res.push_back(nums[w.front()]);
                l++;
            }
            r++;
        }
        return res;
        
    }
};
