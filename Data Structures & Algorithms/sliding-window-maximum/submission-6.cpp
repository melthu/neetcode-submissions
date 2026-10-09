class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        std::priority_queue<pair<int, int>> heap;
        for (int i = 0; i < k; i++) {
            heap.push({nums[i], i});
        }

        std::vector<int> res;
        res.push_back(heap.top().first);
        for (int r = k; r < nums.size(); r++) {
            heap.push({nums[r], r});

            while (heap.top().second <= r - k) {
                heap.pop();
            }
            res.push_back(heap.top().first);
        }
        return res;


        
    }
};
