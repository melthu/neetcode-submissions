class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        std::vector<int> counts(26, 0);
        for (char task : tasks) {
            counts[task - 'A']++;
        }

        std::priority_queue<int> heap;
        for (int count : counts) {
            if (count > 0) {
                heap.push(count);
            }
        }

        std::queue<std::pair<int, int>> q;
        
        int time = 0;
        while (!heap.empty() or !q.empty()) {
            if (!heap.empty()) {
                int cnt = heap.top() - 1;
                if (cnt > 0) {
                    q.push({cnt, time + n});
                }
                heap.pop();
            } else {
                time = q.front().second;
            }

            if (!q.empty() and q.front().second == time) {
                heap.push(q.front().first);
                q.pop();
            }
            time++;
        }
        return time;
    }
};
