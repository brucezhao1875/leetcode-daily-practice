class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        remaining_prerequisites = [ 0 for _ in range(numCourses) ]
        unlocked_courses = defaultdict(list)
        for course,prerequisite in prerequisites:
            remaining_prerequisites[course] += 1
            unlocked_courses[prerequisite].append(course)

        available_courses = deque()
        for course_id in range(numCourses):
            if remaining_prerequisites[course_id] == 0 :
                available_courses.append(course_id)

        result = []
        while available_courses:
            current_course = available_courses.popleft()
            result.append(current_course)
            for unlocked_course in unlocked_courses[current_course]:
                remaining_prerequisites[unlocked_course] -= 1
                if remaining_prerequisites[unlocked_course] == 0 :
                    available_courses.append(unlocked_course)
        return result if len(result) == numCourses else []