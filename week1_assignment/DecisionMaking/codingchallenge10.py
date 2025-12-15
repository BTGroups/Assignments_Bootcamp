def calculate_class(average : float) -> str:
    if average >= 60:
        return "1st Class"
    elif average >= 50:
        return "2nd Class"
    elif average >= 35:
        return "Pass Class"
    else:
        return "Fail"
    

if __name__ == "__main__":
    try: 
        name = input("Enter the student's name: ")
        s1 = float(input("Enter score for Subject 1: "))
        s2 = float(input("Enter score for Subject 2: "))
        s3 = float(input("Enter score for Subject 3: "))

        total = s1 + s2 + s3 
        average = total / 3 

        student_class = calculate_class(average)
    except ValueError:
        print("ValueError: Please enter valid numeric scores.")
    except Exception as e:
        print(f"Unexpected Error ({type(e).__name__}): {e}")

