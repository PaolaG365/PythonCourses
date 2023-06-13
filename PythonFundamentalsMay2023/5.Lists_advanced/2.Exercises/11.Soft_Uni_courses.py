def add(courses, lesson_title): return courses.append(lesson_title)


def insert_lesson(courses, lesson, target_index): return courses.insert(target_index, lesson)


def remove_lesson(courses, lesson):
    if f"{lesson}-Exercise" in courses:
        courses.remove(f"{lesson}-Exercise")
    courses.remove(lesson)
    return courses


def swap(courses, lesson1, lesson2):
    lesson1_index = 0
    lesson2_index = 0

    for course in range(len(courses)):
        if lesson1 == courses[course]:
            lesson1_index = course
        if lesson2 == courses[course]:
            lesson2_index = course

    courses[lesson1_index], courses[lesson2_index] = courses[lesson2_index], courses[lesson1_index]

    if len(courses) - 1 > lesson1_index:
        if courses[lesson1_index + 1] == f"{lesson1}-Exercise":
            courses.pop(lesson1_index + 1)
            courses.insert(lesson2_index + 1, f"{lesson1}-Exercise")
    if len(courses) - 1 > lesson2_index:
        if courses[lesson2_index + 1] == f"{lesson2}-Exercise":
            courses.pop(lesson2_index + 1)
            courses.insert(lesson1_index + 1, f"{lesson2}-Exercise")

    return courses


def exercise(courses, lesson_exercise):
    if lesson_exercise in courses and f"{lesson_exercise}-Exercise" not in courses:
        lesson_exercise_index = courses.index(lesson_exercise)
        courses.insert(lesson_exercise_index + 1, f"{lesson_exercise}-Exercise")
    elif lesson_exercise not in courses:
        courses.append(lesson_exercise)
        courses.append(f"{lesson_exercise}-Exercise")

    return courses


courses_and_exercises = input().split(", ")
command = input()

while command != "course start":
    course_event = command.split(":")
    action = course_event[0]
    course_title = course_event[1]

    if action == "Add":
        if course_title not in courses_and_exercises:
            add(courses_and_exercises, course_title)

    elif action == "Insert":
        if course_title not in courses_and_exercises:
            index = int(course_event[2])
            insert_lesson(courses_and_exercises, course_title, index)

    elif action == "Remove":
        if course_title in courses_and_exercises:
            remove_lesson(courses_and_exercises, course_title)

    elif action == "Swap":
        lesson_to_swap_with = course_event[2]
        if course_title in courses_and_exercises and lesson_to_swap_with in courses_and_exercises:
            swap(courses_and_exercises, course_title, lesson_to_swap_with)

    elif action == "Exercise":
        exercise(courses_and_exercises, course_title)

    command = input()

for course2 in range(1, len(courses_and_exercises) + 1):
    print(f"{course2}.{courses_and_exercises[course2 - 1]}")
