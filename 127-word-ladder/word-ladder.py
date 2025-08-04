class Solution:
    '''
    这个跟#433 一模一样,graph bfs.
    '''
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        bank = set(wordList)
        visited = set()
        queue = deque([(beginWord,1)])
        visited.add(beginWord)
        
        while queue:
            current, steps = queue.popleft() 
            if current == endWord:
                return steps
            for i in range(len(current)):
                for c in range(ord('a'),ord('z')+1):
                    if chr(c) != current[i]:
                        next_seq = current[:i] + chr(c) + current[i+1:]
                        if next_seq in bank and next_seq not in visited:
                            visited.add(next_seq)
                            queue.append((next_seq,steps+1))
        return 0
