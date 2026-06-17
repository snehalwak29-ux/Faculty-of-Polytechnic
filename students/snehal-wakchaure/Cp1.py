def format_marks(m1, m2, m3):
    return str(m1) + "," + str(m2) + "," + str(m3)


def letter_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"



def result(a):
    if a >= 75:
        return "DISTINCTION"
    elif avg >= 35:
        return "PASS"
    else:
        return "FAIL"


def avg(m1, m2, m3):
    return round (m1 + m2 + m3) / 3


def is_prime(n):
    if n < 2:
        return False
    if n == 2: 
        return True
    if n % 2 == 0: 
        return False
   is_prime = True
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            is_prime = False 
            break          
            
    return is_prime

    
    





  
