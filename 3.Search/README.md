# Search（查找算法）
## 一、查找表
### 考虑的基本数据结构
**第一类：查找有无--set**

元素'a'是否存在，通常用set：集合

set只存储健，而不需要对应其相应的值

set中的键不允许重复

**第二类：查找对应关系（键值对应）--dict**

元素'a'出现了几次：dict：字典

dict中的键不允许重复

**第三类：改变映射关系--map**
通过将原有序列的映射关系统一表示为其他

### 例题
- [349.两个数组的交集](https://github.com/CRuJia/LeetCode/blob/master/3.Search/349.Intersection%20of%20Two%20Arrays.py)
- [350.两个数组的交集](https://github.com/CRuJia/LeetCode/blob/master/3.Search/350.Intersection%20of%20Two%20Arrays%20II.py)
- [242.有效的字母异位词](https://github.com/CRuJia/LeetCode/blob/master/3.Search/242.Valid%20Anagram.py)
- [202.快乐数](https://github.com/CRuJia/LeetCode/blob/master/3.Search/202.Happy%20Number.py)
- [290.单词规律](https://github.com/CRuJia/LeetCode/blob/master/3.Search/290.Word%20Pattern.py)
- [205.同构字符串](https://github.com/CRuJia/LeetCode/blob/master/3.Search/205.Isomorphic%20Strings.py) 和290类似，使用map函数
- [451.根据字符出现频率排序](https://github.com/CRuJia/LeetCode/blob/master/3.Search/451.Sort%20Characters%20By%20Frequency.py)

## 二、对撞指针
## 三、滑动数组
## 四、二分查找

查找属于算法题中常见的算法，怎么最大化查找效率和写出bugfree的代码是最难的一部分。一般的查找方法有顺序查找、二分查找和双指针。

一般二分查找的对象是有序或者由有序部分变化的。

### 代码模版
```python
class Solution:
    def firstBadVersion(self, arr):
        # 第一点
        lo, hi = 0, len(arr)-1
        while lo < hi:
            # 第二点
            mid = (lo+hi) // 2
            # 第三点
            if f(x):
                lo = mid + 1
            else:
                hi = mid
        return lo
```

- [35.搜索插入位置](https://github.com/CRuJia/LeetCode/blob/master/3.Search/35.Search%20Insert%20Position.py)
- [ ] [410.分割数组的最大值](https://github.com/CRuJia/LeetCode/blob/master/3.Search/410.Split%20Array%20Largest%20Sum.py)
- [540.有序数组中的单一元素](https://github.com/CRuJia/LeetCode/blob/master/3.Search/540.Single%20Element%20in%20a%20Sorted%20Array.py)
