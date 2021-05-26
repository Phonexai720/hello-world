import numpy as np

data_tyte = [(' name', 's15'),('class', int),('heighr', float)]

students_details =[('jame', 5, 48.5), ('nail', 6,52.5),('paul',5,42.1),('pit',5,40.11)]

students = np.array(students_details, dtype=data_type)

print ("original array:")

print(students)

print("Sort by height")

print(np,sort(studens,order='height'))
