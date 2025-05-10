def angryProfessor(k, a):
    #code here
    on_time_students = sum(1 for time in a if time <= 0)
    return "YES" if on_time_students < k else "NO"

# Run tests
print(angryProfessor(3,[-1,-3,4,2]))

