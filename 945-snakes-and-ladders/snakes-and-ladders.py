class Solution:
    '''

    这是个垃圾算法题，挺没劲的。直接把它提交过去，以后也不要看。不要浪费时间在这样的破题上。

    '''
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        vis = [False] * (n * n + 1)
        vis[1] = True  # 题目保证起点没有蛇梯，不写也可以
        q = [1]  # 起点
        step = 0
        while q:
            tmp = q
            q = []
            for x in tmp:
                if x == n * n:  # 终点
                    return step
                for y in range(x + 1, min(x + 6, n * n) + 1):
                    r, c = divmod(y - 1, n)
                    if r % 2:
                        c = n - 1 - c  # 奇数行从右到左
                    nxt = board[-1 - r][c]
                    if nxt < 0:
                        nxt = y
                    if not vis[nxt]:
                        vis[nxt] = True  # 有环的情况下，避免死循环
                        q.append(nxt)
            step += 1
        return -1  # 无法到达终点
