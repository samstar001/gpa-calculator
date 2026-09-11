

grade_scale = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
    "E": 1,
    "F": 0
}

'''
first_semester = [
    {
        "code": "CPE301",
        "title": "Computer Organization and Architecture",
        "units": 2,
        "grade": "A"
    },

    {
        "code": "EEE321",
        "title": "Analogue Electronic Circuits",
        "units": 2,
        "grade": "B"
    },

    {
        "code": "GET301",
        "title": "Engineering Mathematics III",
        "units": 3,
        "grade": "A"
    },

    {
        "code": "GET305",
        "title": "Engineering Statistics and Data Analytics",
        "units": 3,
        "grade": "B"
    }
]

second_semester = [
    {
        "code": "CPE302",
        "title": "Measurement and Instrumentation",
        "units": 3,
        "grade": "A"
    },

    {
        "code": "EEE322",
        "title": "Digital Electronic Circuits",
        "units": 2,
        "grade": "A"
    },

    {
        "code": "GET302",
        "title": "Engineering Mathematics IV",
        "units": 3,
        "grade": "A"
    },

    {
        "code": "GET306",
        "title": "Renewable Energy",
        "units": 3,
        "grade": "B"
    },

    {
        "code": "ENT312",
        "title": "Venture Creation",
        "units": 2,
        "grade": "B"
    }
]
'''

def calc_quality_point(credit_unit, grade):
    grade_point = grade_scale[grade]
    quality_point = grade_point * credit_unit
    return quality_point


def collect_courses():
    num_of_courses = int(input("How many courses are you entering? "))
    course_list = []
    for course in range(1, num_of_courses + 1):
        print ("\n Course", course)
        course_code = input("Enter the course code: ")
        course_title = input("Enter the course title: ")
        credit_units = int(input("Enter the credit unit: "))
        grade = input("Enter your the course grade (eg. A, B,): ")
        course_data = {
            "code": course_code,
            "title": course_title,
            "units": credit_units,
            "grade": grade
        }
        course_list.append(course_data)
    return course_list

def calc_sgpa(course_list):
    total_quality_points = 0
    total_credit_units = 0

    for course in course_list:
        units = course["units"]
        total_credit_units += units
        grade = course["grade"]
        quality_point = calc_quality_point(units, grade)
        total_quality_points += quality_point
    sgpa = round(total_quality_points / total_credit_units, 2)
    return sgpa, total_quality_points, total_credit_units

def calc_cgpa(total_quality_points, total_credit_units):
    cgpa = round(total_quality_points / total_credit_units, 2)
    return cgpa
def display_semester_result(semester, sgpa, quality_points, credit_units):
    print(f"{semester} SGPA: {sgpa} \n{semester} Quality Points:{quality_points} \n{semester} Credit Units:{credit_units}")


first_semester = collect_courses()
second_semester = collect_courses()

first_sgpa, first_quality_points, first_credit_units = calc_sgpa(first_semester)

second_sgpa, second_quality_points, second_credit_units = calc_sgpa(second_semester)

total_quality_points = first_quality_points + second_quality_points
total_credit_units = first_credit_units + second_credit_units

cgpa = calc_cgpa(total_quality_points, total_credit_units)
print("CGPA:", cgpa)

display_semester_result("First Semester", first_sgpa, first_quality_points, first_credit_units)
display_semester_result("Second Semester", second_sgpa, second_quality_points, second_credit_units)