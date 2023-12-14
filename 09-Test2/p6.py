def f(years,course):
    import json
#years = 21
#course = "statistics"

    file = open("data.json")
    file_content = json.load(file)
    lent = len(file_content)
    student_count = 0
    for i in range(lent):
        diction = file_content[i]
        if int(diction["age"])>= years:
            studies = diction["studies"]
            courses = studies["courses"]
            lent2 = len(courses)
            for j in range(lent2):
                courses_item = courses[j]
                for key,value in courses_item.items():
                    if courses_item[key] == course:
                        sum = 0
                        grades = courses_item["grades"]
                        for k in range(len(grades)):
                            sum += grades[k]
                        avg = sum/len(grades)
                        if avg>=4:
                            student_count +=1
#    file.close()
    return student_count
                   
if __name__ == "__main__":
    # function calls
    print(f(21,"statistics"))
    print(f(18,"programming"))
