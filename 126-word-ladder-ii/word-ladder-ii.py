
class Solution:

    '''
    这个跟#127很像，是graph bfs。
    不同地方在于：要返回所有最短的结果。
    但是一个单词的变化路径有多个路径长度不同的，而路径长度相同的也有多个不同路径。
    这可如何是好？ -- 答案就是你先找出最短长度，然后在最短长度的基础上寻找答案。
    1、最短长度：这个好做，while循环中最快返回的，那就是最短路径。
    2、在最短路径基础上怎么寻找所有答案：for循环，只有还有路径长度可探索时，你再继续往下找。

    但是这么写还是会timeout，原因是dfs会重复搜索。因此又改进了如下。
    '''

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        
        bank = set(wordList)
        
        # BFS构建层级图，记录每个词的所有可能父节点
        neighbors = defaultdict(list)
        visited = {beginWord}
        queue = deque([beginWord])
        found = False
        
        while queue and not found:
            # 当前层访问的所有新词
            current_level = set()
            
            # 处理当前层的所有词
            for _ in range(len(queue)):
                current = queue.popleft()
                
                # 生成所有可能的邻居
                for i in range(len(current)):
                    for c in range(ord('a'), ord('z') + 1):
                        if chr(c) != current[i]:
                            next_word = current[:i] + chr(c) + current[i+1:]
                            
                            if next_word in bank:
                                if next_word == endWord:
                                    found = True
                                
                                # 如果这个词没被访问过
                                if next_word not in visited:
                                    if next_word not in current_level:
                                        current_level.add(next_word)
                                        queue.append(next_word)
                                    # 记录父子关系
                                    neighbors[next_word].append(current)
            
            # 标记当前层的词为已访问
            visited.update(current_level)
        
        # 如果找不到路径
        if not found:
            return []
        
        # DFS回溯构建所有路径
        result = []
        
        def backtrack(word, path):
            if word == beginWord:
                result.append([beginWord] + path)
                return
            
            # 遍历所有可能的父节点
            for parent in neighbors[word]:
                backtrack(parent, [word] + path)
        
        backtrack(endWord, [])
        return result
