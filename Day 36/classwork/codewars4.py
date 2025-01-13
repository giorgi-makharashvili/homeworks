def get_grade(s1, s2, s3):
    average = (s1+s2+s3)//3
    if average >= 90:
        return "A"
    elif average < 90 and average >= 80:
        return "B"
    elif average < 80 and average >= 70:
        return "C"
    elif average < 70 and average >= 60:
        return "D"
    elif average < 60 and average >= 0:
        return "F"