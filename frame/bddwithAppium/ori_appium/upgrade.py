def isRegister(phone):
    pass


def studentCurriculums(student, year: int, quarters: list, genre_list: list):
    """查找学生的课程

    Args:
        student ([type]): 学生 
        year (int): 年
        quarters (list): 季度
        genre_list (list): 课程类型

    Returns:
        [type]: [description]
    """
    return [], 0


def hasStudent():
    pass


def isFinish(student):
    pass


def getStudents():
    yield 1


def isSameGrade(student, curriculums=None):
    pass


def maxGrade(curriculums):
    return max([curriculum.grade for curriculum in curriculums])


def curriculumIsSameGrade(curriculums):
    return True if sum([curriculum.grade for curriculum in curriculums]
                       ) % len(curriculums) == 0 else False


def main():
    for student in getStudents():
        if not isRegister(student.phone):
            student.grade += 1
            continue
        # 2021 - 暑秋 - 专题体验课,短期正价课,系统正价课
        student_curriculums, length = studentCurriculums(
            student, 2021, [3, 4], [1, 8, 9])
        if 0 != length:
            student.grade = maxGrade(student_curriculums)
            continue
        # 2020 - 全年 - 专题体验课,短期正价课,系统正价课
        student_curriculums, length = studentCurriculums(
            student, 2020, [1, 2, 3, 4], [1, 8, 9])
        if 0 != length:
            student.grade = maxGrade(student_curriculums) + 1
            continue
        # 2021 - 暑秋 - 专题活动课,免费公开课
        student_curriculums, length = studentCurriculums(
            student, 2021, [3, 4], [2, 3])
        if 0 != length:
            if curriculumIsSameGrade(student_curriculums):
                student.grade = maxGrade(student_curriculums) + 1
                continue
        # 2020 - 暑秋 - 专题活动课,免费公开课
        student_curriculums, length = studentCurriculums(
            student, 2020, [3, 4], [2, 3])
        if 0 != length:
            if curriculumIsSameGrade(student_curriculums):
                student.grade = maxGrade(student_curriculums) + 1
                continue
        student.grade += 1
