class Solution:
    '''
    最直接的解法：
        for each word in words:
            for each start point in board:
                for all directions :
                    if 相应位置匹配 then 继续

    这个复杂度是O(words.length)*O(m*n)* direction^{word.length} = O(3*10^4*12*12*3^{10}) = 10^{11}
    这个肯定是不行。那么在这个基础上进行改进。

    #Trie的使用（错误的计算方法）
    1、首先注意到啊，这里有个最大的数字是words.length = 3*10^4 ; 
    2、word的每个字符均为小写字母（26个）
    3、word的长度<=10.
    这意味着：前缀相同的比例很大。举个例子讲：这颗Trie的最复杂的情况为： 
        -- level 0 - level 3 ，共4层，尽量不同，就可覆盖超过3*10^4的不同word的情况
    
    那么words.length的匹配复杂度 --转换为--> 直接跟一颗树做比较。
    1、O(m*n)还在
    2、当前字符和Trie的比较：3 * 26 （3个方向，跟Trie的当前层的可能的26个字符做比较）
    3、如上所计算，最复杂的层数是：4层；
    4、因此，复杂度为：O(m*n) * O((3*26)^4) = 10^9 依然很大啊。

    #Trie的使用（正确的计算方法）
    老师傅遇到新问题。
    先回答我： 'a'  in children的复杂度多少？其中children是Trie当前节点的子节点，是hash。
    答案是：x in hash的复杂度是O(1) ，它的计算过程是：x -> key(x) , 然后查看children中的data[key],
    这个过程是直接定位，当然是O(1)
    好了，那么上面计算的每层3*26， 实际上的复杂度是每层3
    因此整体的复杂度为：
    O(m*n) * O((3)^L) = 10^7 ，实际上会更小，因为L不会这么大。 
    
    #review一遍，关键的修改在哪里：
    从"每个word在board里边找得到不？" 变化为： "board中的三个字符在Trie中能找到不？"
    前面的复杂度是对word遍历； 后面，因为变成hash查找，变为O(1)。变化最大的就在这。
    反过来找，从n个在1个中找 变成  1个在n个中找（用hash）

    #further more
    如果可以用hash，我也可以反过来用hash。
    回到方法1，做个改进
        for each word in words:
            for each start point in board:
                把这里的"for all directions ... " 换成hash操作，O(1)；
                那么这里就变成 ( O(1) )^L

    这个复杂度是O(words.length)*O(m*n)* O(1)^{word.length} = 3 * 10^6 *  (O(1))^L
    是不是也可以呢？

    这想法好是好，但是有两个不足：
    1、O(1)这个实现，它还要对direction的4个方向中进行一个方向的排除，这个操作，麻烦。
    2、O(1)的指数级，这个一不小心就会窜上天际了啊。 这个好理解吧？毕竟2^10 = 10^3了。
    因此啊，这种O(1)的指数级，算了吧，玩不转，别想了。

    '''
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        for word in words:
            t = trie
            for w in word:
                if w not in t:
                    t[w] = {}
                t = t[w]
            t["end"] = 1
        #print(trie)
        res = []
        row = len(board)
        col = len(board[0])
        def dfs(i, j, trie, s):
            #print(i, j, trie, s)
            c = board[i][j]
            if c not in trie: return
            trie = trie[c]
            if "end" in trie and trie["end"] == 1:
                res.append(s + c)
                trie["end"] = 0 # 防止重复数组加入
            board[i][j] = "#"
            for x, y in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                tmp_i = x + i
                tmp_j = y + j
                if 0 <= tmp_i < row and 0 <= tmp_j < col and board[tmp_i][tmp_j] != "#":
                    dfs(tmp_i, tmp_j, trie, s + c)
            board[i][j] = c
        for i in range(row):
            for j in range(col):
                dfs(i, j, trie, "")
        return res
