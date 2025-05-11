def gradingStudents(grades):
    """
    Rounds each grade according to the university policy:
      - If the grade is below 38, no rounding is applied.
      - Otherwise, if the next multiple of 5 is within 2 points, round up to it.
    """
    result = []
    for n in grades:
        if n < 38:
            
            result.append(n)
        else:
           
            next_mult_5 = ((n // 5) + 1) * 5
           
            if next_mult_5 - n < 3:
                result.append(next_mult_5)
            else:
                result.append(n)
    return result


if __name__ == "__main__":
    grades = [73, 67, 38, 33]
    print(gradingStudents(grades))  
