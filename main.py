

grade_scale = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
    "E": 1,
    "F": 0
}

courses = [
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


def calc_quality_point(credit_unit, grade):
    grade_point = grade_scale[grade]
    quality_point = grade_point * credit_unit
    return quality_point

def calc_sgpa(courses):
    total_quality_points = 0
    total_credit_units = 0

    for course in courses:
        units = course["units"]
        total_credit_units += units
        grade = course["grade"]
        quality_point = calc_quality_point(units, grade)
        total_quality_points += quality_point
    sgpa = round(total_quality_points / total_credit_units, 2)
    return sgpa
# print(calc_sgpa(courses))

print(calc_sgpa(second_semester))