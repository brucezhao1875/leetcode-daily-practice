class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 每门课程需要的前置课程数量
        remaining_prerequisites = [0] * numCourses
        
        # 完成某门课程后可以解锁的课程列表
        unlocked_courses = defaultdict(list)
        
        # 构建图：course需要prerequisite作为前置课程
        for course, prerequisite in prerequisites:
            remaining_prerequisites[course] += 1
            unlocked_courses[prerequisite].append(course)
        
        # 找到所有没有前置课程的课程（可以直接开始学习）
        available_courses = deque()
        for course_id in range(numCourses):
            if remaining_prerequisites[course_id] == 0:
                available_courses.append(course_id)
        
        # 统计已完成的课程数量
        completed_courses = 0
        
        # 拓扑排序：逐一完成课程
        while available_courses:
            current_course = available_courses.popleft()
            completed_courses += 1
            
            # 完成当前课程后，检查解锁的课程
            for unlocked_course in unlocked_courses[current_course]:
                remaining_prerequisites[unlocked_course] -= 1
                # 如果某门课程的所有前置课程都完成了，加入可学习队列
                if remaining_prerequisites[unlocked_course] == 0:
                    available_courses.append(unlocked_course)
        
        # 如果所有课程都能完成，返回True
        return completed_courses == numCourses