title1 = "GRADE SHEET PROGRAM"

print(
    "=====" * 32
)

print(
    "{:^160}".format(title1)
)

print(
    "=====" * 32
)

print(
    "Welcome to the Grade Sheet Program!",
    "You can calculate your semestral grade here for a certain subject, just follow the instructions below.",
    "Instructions: Enter your personal information before inputting the value of your grades.",
    "Please only put what the program requires. Make sure that your answers are valid. ",
    "After inputting, the program will instantly show your computed grades."
    "Thank you and have fun using the program!"
)

print(
    "=====" * 32
)

while True:
    first_name = str(input("Enter your first name: "))
    middle_name = str(input("Enter your middle name: "))
    last_name = str(input("Enter your last name: "))
    grade = str(input("Enter your grade level: "))
    section = str(input("Enter your section: "))
    student_no = str(input("Enter your student number: "))
    choice = str(input("Are your information correct? Yes or No? "))
    if choice == "Yes":
        print(
            "=====" * 32
        )
        print(
            "-----",
            "PROFILE",
            "-----"
        )
        print(
            "Name:",
            first_name,
            middle_name,
            last_name,
            "\nGrade & Section:",
            grade,
            section,
            "\nStudent Number: ",
            student_no
        )
        print(
            "=====" * 32
        )
        break
    elif choice == "yes":
        print(
            "=====" * 32
        )
        print(
            "-----",
            "PROFILE",
            "-----"
        )
        print(
            "Name:",
            first_name,
            middle_name,
            last_name,
            "\nGrade & Section:",
            grade,
            section,
            "\nStudent Number: ",
            student_no
        )
        print(
            "=====" * 32
        )
        break
    elif choice == "YES":
        print(
            "=====" * 32
        )
        print(
            "-----",
            "PROFILE",
            "-----"
        )
        print(
            "Name:",
            first_name,
            middle_name,
            last_name,
            "\nGrade & Section:",
            grade,
            section,
            "\nStudent Number: ",
            student_no
        )
        print(
            "=====" * 32
        )
        break
    else:
        continue

print(
    "CALCULATION FOR MIDTERM GRADE",
    "\n"
)

print(
    "MIDTERM WRITTEN WORKS:"
)

while True:
    m_ww_1 = float(input("Enter your grade for Midterm Written Work #1: "))
    if m_ww_1 < 0:
        print(
            "Invalid Grade. Try again."
        )
        continue
    elif m_ww_1 > 50:
        print(
            "Invalid Grade. Try again."
        )
        continue
    else:
        break

while True:
    m_ww_2 = float(input("Enter your grade for Midterm Written Work #2: "))
    if m_ww_2 < 0:
        print(
            "Invalid Grade. Try again."
        )
        continue
    elif m_ww_2 > 50:
        print(
            "Invalid Grade. Try again."
        )
        continue
    else:
        break


def sum1(m_ww_1, m_ww_2):
    return (m_ww_1 + m_ww_2)


sum1 = float(sum1(m_ww_1, m_ww_2))


def per1(m_ww_1, m_ww_2):
    return ((sum1/100) * 100)


percentage1 = float(per1(m_ww_1, m_ww_2))


def wg1(m_ww_1, m_ww_2):
    return (percentage1 * 0.25)


weight1 = float(wg1(m_ww_1, m_ww_2))

print(
    "The sum of your Midterm Written Works is",
    sum1
)

print(
    "The average of your Midterm Written Works is",
    percentage1,
    end="%\n"
)

print(
    "The weighted percentage of your Midterm Written Works is",
    weight1,
    end="%\n"
)

print(
    "\n"
)

print(
    "MIDTERM PERFORMANCE TASKS:"
)

while True:
    m_pt_1 = float(input("Enter your grade for Midterm Performance Task #1: "))
    if m_pt_1 < 0:
        print(
            "Invalid Grade. Try again."
        )
        continue
    elif m_pt_1 > 50:
        print(
            "Invalid Grade. Try again."
        )
        continue
    else:
        break

while True:
    m_pt_2 = float(input("Enter your grade for Midterm Performance Task #2: "))
    if m_pt_2 < 0:
        print(
            "Invalid Grade. Try again."
        )
        continue
    elif m_pt_2 > 50:
        print(
            "Invalid Grade. Try again."
        )
        continue
    else:
        break


def sum2(m_pt_1, m_pt_2):
    return (m_pt_1 + m_pt_2)


sum2 = float(sum2(m_pt_1, m_pt_2))


def per2(m_pt_1, m_pt_2):
    return ((sum2/100) * 100)


percentage2 = float(per2(m_pt_1, m_pt_2))


def wg2(m_pt_1, m_pt_2):
    return (percentage2 * 0.45)


weight2 = float(wg2(m_pt_1, m_pt_2))

print(
    "The sum of your Midterm Performance Tasks is",
    sum2
)

print(
    "The average of your Midterm Performance Tasks is",
    percentage2,
    end="%\n"
)

print(
    "The weighted percentage of your Midterm Performance Tasks is",
    weight2,
    end="%\n"
)

print(
    "\n"
)

print(
    "MIDTERM MAJOR EXAM:"
)

while True:
    m_me = float(input("Enter your grade for Midterm Major Exam: "))
    if m_me < 0:
        print(
            "Invalid Grade. Try again."
        )
        continue
    elif m_me > 50:
        print(
            "Invalid Grade. Try again."
        )
        continue
    else:
        break


def per3(m_me):
    return ((m_me/50) * 100)


percentage3 = float(per3(m_me))


def wg3(m_me):
    return (percentage3 * 0.30)


weight3 = float(wg3(m_me))

print(
    "The score of your Midterm Major Exam is",
    m_me
)

print(
    "The percentage of your Midterm Major Exam is",
    percentage3,
    end="%\n"
)

print(
    "The weighted percentage of your Midterm Major Exam is",
    weight3,
    end="%\n"
)

print(
    "=====" * 32
)


def sumt1(sum1, sum2, m_me):
    return (sum1 + sum2 + m_me)


sumt1 = float(sumt1(sum1, sum2, m_me))


def tt1(weight1, weight2, weight3):
    return (weight1 + weight2 + weight3)


total1 = float(tt1(weight1, weight2, weight3))

print(
    "-----",
    "MIDTERM GRADES",
    "-----"
)

print(
    "Total Sum of Midterm Grades: ",
    sumt1
)

print(
    "Midterm Written Works (%): ",
    percentage1,
    end="%\n"
)

print(
    "Midterm Performance Tasks (%): ",
    percentage2,
    end="%\n"
)

print(
    "Midterm Major Exam (%): ",
    percentage3,
    end="%\n"
)

print(
    "Midterm Grade: ",
    total1,
    end="%\n"
)

if total1 >= 89.5 <= 100.0:
    print(
        "Letter Grade: A",
        "\nRemarks: Outstanding"
    )
elif total1 >= 79.5 <= 89.4:
    print(
        "Letter Grade: B",
        "\nRemarks: Excellent"
    )
elif total1 >= 69.5 <= 79.4:
    print(
        "Letter Grade: C",
        "\nRemarks: Average"
    )
elif total1 >= 59.5 <= 69.4:
    print(
        "Letter Grade: D",
        "\nRemarks: Poor"
    )
elif total1 >= 0 <= 59.4:
    print(
        "Letter Grade: E",
        "\nRemarks: Failed"
    )
else:
    pass

print(
    "=====" * 32,
)

print(
    "CALCULATION FOR FINAL GRADE",
    "\n"
)

print(
    "FINAL WRITTEN WORKS:"
)

while True:
    f_ww_1 = float(input("Enter your grade for Final Written Work #1: "))
    if f_ww_1 < 0:
        print(
            "Invalid Grade. Try again."
        )
        continue
    elif f_ww_1 > 50:
        print(
            "Invalid Grade. Try again."
        )
        continue
    else:
        break

while True:
    f_ww_2 = float(input("Enter your grade for Final Written Work #2: "))
    if f_ww_2 < 0:
        print(
            "Invalid Grade. Try again."
        )
        continue
    elif f_ww_2 > 50:
        print(
            "Invalid Grade. Try again."
        )
        continue
    else:
        break


def sum3(f_ww_1, f_ww_2):
    return (f_ww_1 + f_ww_2)


sum3 = float(sum3(f_ww_1, f_ww_2))


def per4(f_ww_1, f_ww_2):
    return ((sum3/100) * 100)


percentage4 = float(per4(f_ww_1, f_ww_2))


def wg4(f_ww_1, f_ww_2):
    return (percentage4 * 0.25)


weight4 = float(wg4(f_ww_1, f_ww_2))

print(
    "The sum of your Final Written Works is",
    sum3
)

print(
    "The average of your Final Written Works is",
    percentage4,
    end="%\n"
)

print(
    "The weighted percentage of your Final Written Works is",
    weight4,
    end="%\n"
)

print(
    "\n"
)

print(
    "FINAL PERFORMANCE TASKS:"
)

while True:
    f_pt_1 = float(input("Enter your grade for Final Performance Task #1: "))
    if f_pt_1 < 0:
        print(
            "Invalid Grade. Try again."
        )
        continue
    elif f_pt_1 > 50:
        print(
            "Invalid Grade. Try again."
        )
        continue
    else:
        break

while True:
    f_pt_2 = float(input("Enter your grade for Final Performance Task #2: "))
    if f_pt_2 < 0:
        print(
            "Invalid Grade. Try again."
        )
        continue
    elif f_pt_2 > 50:
        print(
            "Invalid Grade. Try again."
        )
        continue
    else:
        break


def sum4(f_pt_1, f_pt_2):
    return (f_pt_1 + f_pt_2)


sum4 = float(sum4(f_pt_1, f_pt_2))


def per5(f_pt_1, f_pt_2):
    return ((sum4/100) * 100)


percentage5 = float(per5(f_pt_1, f_pt_2))


def wg5(f_pt_1, f_pt_2):
    return (percentage5 * 0.45)


weight5 = float(wg5(f_pt_1, f_pt_2))

print(
    "The sum of your Final Performance Tasks is",
    sum4
)

print(
    "The average of your Final Performance Tasks is",
    percentage5,
    end="%\n"
)

print(
    "The weighted percentage of your Final Performance Tasks is",
    weight5,
    end="%\n"
)

print(
    "\n"
)

print(
    "FINAL MAJOR EXAM:"
)

while True:
    f_me = float(input("Enter your grade for Final Major Exam: "))
    if f_me < 0:
        print(
            "Invalid Grade. Try again."
        )
        continue
    elif f_me > 50:
        print(
            "Invalid Grade. Try again."
        )
        continue
    else:
        break


def per6(f_me):
    return ((f_me/50) * 100)


percentage6 = float(per6(f_me))


def wg6(f_me):
    return (percentage6 * 0.30)


weight6 = float(wg6(m_me))

print(
    "The score of your Midterm Major Exam is",
    f_me
)

print(
    "The percentage of your Midterm Major Exam is",
    percentage6,
    end="%\n"
)

print(
    "The weighted percentage of your Midterm Major Exam is",
    weight6,
    end="%\n"
)

print(
    "=====" * 32
)


def sumt2(sum3, sum4, f_me):
    return (sum3 + sum4 + f_me)


sumt2 = float(sumt2(sum3, sum4, f_me))


def tt2(weight4, weight5, weight6):
    return (weight4 + weight5 + weight6)


total2 = float(tt2(weight4, weight5, weight6))

print(
    "-----",
    "FINAL GRADES",
    "-----"
)

print(
    "Total Sum of Final Grades: ",
    sumt2
)

print(
    "Final Written Works (%): ",
    percentage4,
    end="%\n"
)

print(
    "Final Performance Tasks (%): ",
    percentage5,
    end="%\n"
)

print(
    "Final Major Exam (%): ",
    percentage6,
    end="%\n"
)

print(
    "Final Grade: ",
    total2,
    end="%\n"
)

if total2 >= 89.5 <= 100.0:
    print(
        "Letter Grade: A",
        "\nRemarks: Outstanding"
    )
elif total2 >= 79.5 <= 89.4:
    print(
        "Letter Grade: B",
        "\nRemarks: Excellent"
    )
elif total2 >= 69.5 <= 79.4:
    print(
        "Letter Grade: C",
        "\nRemarks: Average"
    )
elif total2 >= 59.5 <= 69.4:
    print(
        "Letter Grade: D",
        "\nRemarks: Poor"
    )
elif total2 >= 0 <= 59.4:
    print(
        "Letter Grade: E",
        "\nRemarks: Failed"
    )
else:
    pass

print(
    "=====" * 32
)

title2 = "SUMMARY OF GRADES"

print(
    "{:^160}".format(title2)
)

print(
    "=====" * 32
)

print(
    "Name:",
    first_name,
    middle_name,
    last_name,
    "\nGrade & Section:",
    grade,
    section,
    "\nStudent Number: ",
    student_no
)


def sumt3(sumt1, sumt2):
    return (sumt1 + sumt2)


sumt3 = float(sumt3(sumt1, sumt2))


def tt3(total1, total2):
    return (total1 + total2)


total3 = float(tt3(total1, total2))


def sem(total3):
    return ((total3/200) * 100)


sem_grade = sem(total3)

print(
    "Midterm Grade: ",
    total1,
    end="%\n"
)

print(
    "Final Grade: ",
    total2,
    end="%\n"
)

print(
    "Total Sum of Grade: ",
    sumt3
)

print(
    "Semestral Grade: ",
    sem_grade,
    end="%\n"
)

if sem_grade >= 89.5 <= 100.0:
    print(
        "Letter Grade: A",
        "\nRemarks: Outstanding"
    )
elif sem_grade >= 79.5 <= 89.4:
    print(
        "Letter Grade: B",
        "\nRemarks: Excellent"
    )
elif sem_grade >= 69.5 <= 79.4:
    print(
        "Letter Grade: C",
        "\nRemarks: Average"
    )
elif sem_grade >= 59.5 <= 69.4:
    print(
        "Letter Grade: D",
        "\nRemarks: Poor"
    )
elif sem_grade >= 0 <= 59.4:
    print(
        "Letter Grade: E",
        "\nRemarks: Failed"
    )
else:
    pass

print(
    "=====" * 32
)

print(
    "Thanks for using the Grade Sheet Program!"
)

print(
    "=====" * 32
)
