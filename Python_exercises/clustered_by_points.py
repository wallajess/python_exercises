points = {"Paul": 15, "Frank": 44, "Tim": 20, "Anna": 29}

def cluster_by_points(points: dict) -> dict:
    clustered = dict()
    for number in range(0, 100, 10):
        students = []
        for student in points.keys():
            if round(points[student], 10) == number:
                students += [student]
        if students != []:
            clustered[number] = students
    return clustered

    #for student in points.keys():
     #   if points[student] <= 10:
      #      += student 
       # elif 10 > points[student] <= 20:
        #    clustered[10] += student
        #elif 20 > points[student] <= 30:
        #    clustered[20] += student
        #elif 30 > points[student] <= 40:
        #    clustered[30] += student
        #elif 40 > points[student] <= 50:
        #    clustered[40] += student
    #return clustered

print(cluster_by_points(points))
