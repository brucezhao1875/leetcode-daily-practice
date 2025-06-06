class Solution:
    '''
    贪心算法能不能用，
    贪心算法：最大的分成两份，再挑最大的分。以case[9]为例，贪心算法不能工作。
    不能工作的原因是贪心算法看不到全局。

    全局来看：计算最终堆数、理论上的最优值。所有低于最优值的不参与运算。
    例2【2,4,8,2】，划分4次后呈8堆，理论最小值2；划分时按照理论值划分，可以。
    例1【9】，理论值3，按照3划分
    这个方法没有证明，试一下看。
    例3，[100,1,1,1,1] ，划分1次，则划分为【20,80,1,1,1,1】，显然不行，最优的是【50,50,1,1,1,1】

    继续改进，将小于理论最优值的不参与计算，则：
    例3 【100,1,1,1,1】 -> [100]分1次，理论值50，
    例4 【100,200,1,1,1,1】 -> [100,200]分1次，理论值100，可行。
    例5 【50,200,1,1,1,1】 -> [50,200]分1次，理论值83, 筛选50 -> [200]分1次 -> [100,100]，可行。
    总结算法：
    1、根据理论最小值逐步筛选掉不参与划分的，直到所有元素都大于理论值
    2、
    例6【100,200】拆4次，则理论值300/6=50，这个做法可行。
    例7【101,200】拆4次，理论值50


    这个算法，在“重复删除无用元素”步骤是正确的，没有问题。
    但是等到所有元素大于理论值之后的操作，怎么拆分？算法并没有描述清楚。
    所以，这个算法并没有触及到本质。

    让我们回到起点。最后查看题解，说的是：“1900分左右的二分法题目挺多的”， 说明这是个套路题：二分法。
    二分法实际上就是遍历，只不过是复杂度从O(n)降为O(logn)的遍历。
    这是个套路。接下来仔细研究这个套路。
    
    假设有x个球，我要让它分成每堆最多m个，我需要做的最小操作次数是多少？
    最佳操作是：每次刚好取出m个。这是因为：如果取出的球数＞m，则等下还要对这一小堆进行拆分；如果取出的球<m，那么操作次数不会比刚好取出m个更少。
    因此，最佳操作是：每次刚好取出m个。
    
    这么来看，要操作的次数：(x-1)//m 。 
    如果x%m==0，那么取值x//m-1 ； 如果x%m≠0，那么取值x//m 。
    这2种情形可以统一为写法： (x-1)//m 


    '''
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def check(m):
            cnt = 0
            for x in nums:
                cnt += (x-1) // m 
            return cnt <= maxOperations
        
        left,right = 0, max(nums)
        while left + 1 < right :
            mid = ( left + right ) // 2
            if check(mid):
                right = mid
            else:
                left = mid
        return right

        