def secondgrade(students, grades):
    pairs = list(zip(students, grades))
    unique_grades = sorted({g for _, g in pairs})
    if len(unique_grades) < 2:
        return []
    second_low = unique_grades[1]
    names = [name for name, g in pairs if g == second_low]
    return sorted(names)


if __name__ == "__main__":
    student = ["S ROY", "B BOSE", "N KAR", "C DUTTA", "G GHOSH"]
    grade = [1, 3, 2, 1, 1]
    result1 = secondgrade(student, grade)
    for name in result1:
        print(name)

