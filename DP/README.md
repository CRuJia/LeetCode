# DP(动态规划)

动态规划常常适用于**有重叠子问题**和**最优子结构**性质的问题。动态规划问题所耗时间往往远远少于朴素解法。

## 主要思想

若要解决一个给定问题，我们需要解决其不同部分（子问题），在根据子问题的解决得以得出原问题的解。动态规划往往用于优化递归问题，如果运动递归解决的话常常会求解很多重复的子问题，因此利用动态规划的思想可以减少计算量。

动态规划法仅仅解决每个子问题一次，具有天然剪枝的功能，从而减少计算量，一旦某个子问题已经算出，则将其记忆化存储，以便下次需要同一个子问题时直接查表。

## 动态规划模版
- 确定动态规划状态
- 写出状态转移方程（画出状态转移表）
- 考虑初始化条件
- 考虑输出状态
- 考虑对时间、空间的优化（Bonus）

## 注意事项
我们需要理清**子序列**（subsequence）和**子数组（字串、连续序列、substring）**的差别，前者明显比后者要复杂一点，因为前者是不连续的序列，后者是连续的序列，从复杂度来看也很清楚能看到即使穷举子序列也比穷举子数组要复杂很多。
## 例题

- [300.最长上升子序列]()
- [53.最大子序和]()
- [1143. 最长公共子序列]()
- [674.最长连续递增序列]()
- [5.最长回文子串]()
- [516.最长回文子序列]()
- [72.编辑距离]()
- [198.打家劫舍]()
- [213.打家劫舍II]()


## 参考

- [掌握动态规划，助你成为优秀的算法工程师](https://www.jiqizhixin.com/articles/2019-09-29-5)
- [ ] 推荐MIT的动态规划练习资料，这份资料通过动态规划经典的问题让我们很清晰的了解到这个算法的魅力所在，对于新手入门动态规划是一个很不错的资料。[Dynamic Programming Practice Problems](https://people.cs.clemson.edu/~bcdean/dp_practice/)
- 五分钟学算法的动态规划系列:[浅谈什么是动态规划以及相关的「股票」、](https://mp.weixin.qq.com/s?__biz=MzUyNjQxNjYyMg==&mid=2247485288&idx=1&sn=fd043fc723f38bcaecc90d9945981f8a&chksm=fa0e68e9cd79e1ffd965205bb06b1731539bf2e0bbc5991664f5d1d9721b346ec08c85bb9042&scene=21#wechat_redirect)
[算法题 有了四步解题法模板，再也不害怕动态规划! ](https://mp.weixin.qq.com/s?__biz=MzUyNjQxNjYyMg==&mid=2247486904&idx=1&sn=099d5560ab25c0163349dff0c7f51490&chksm=fa0e6239cd79eb2fe6e831d7debba60aa906721d592b8766a944ef88bf91bf82568c20d71891&scene=21#wechat_redirect)
[（进阶版）有了四步解题法模板，再也不害怕动态规划！](https://mp.weixin.qq.com/s?__biz=MzUyNjQxNjYyMg==&mid=2247486923&idx=2&sn=6c1c8aeb4db68522e67ddf8c1e933660&chksm=fa0e624acd79eb5cdb410808921609a830b9b9221e813e4eb89cf551ca48f317668d44b095d2&scene=21#wechat_redirect)
- 主要参考的Leetcode 优秀题解：
[动态规划设计方法&&纸牌游戏讲解二分解法](https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/dong-tai-gui-hua-she-ji-fang-fa-zhi-pai-you-xi-jia/)
[动态规划、Manacher 算法](https://leetcode-cn.com/problems/longest-palindromic-substring/solution/zhong-xin-kuo-san-dong-tai-gui-hua-by-liweiwei1419/)
[编辑距离面试题详解](https://leetcode-cn.com/problems/edit-distance/solution/bian-ji-ju-chi-mian-shi-ti-xiang-jie-by-labuladong/)
[打家劫舍 II（动态规划，结构化思路，清晰题解）](https://leetcode-cn.com/problems/house-robber-ii/solution/213-da-jia-jie-she-iidong-tai-gui-hua-jie-gou-hua-/)


