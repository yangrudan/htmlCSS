import stru_stru

res = stru_stru.create()
print(res)
print(res.class_num)
student0 = stru_stru.StudentArray_getitem(res.studentObj,0)
student00 = stru_stru.StudentClass.frompointer(res.studentObj)

print("00: ", student00[0].score)
print("11: ", student00[1].score)
print("22: ", student00[2].score)

print(student0.score)
student1 = stru_stru.StudentArray_getitem(res.studentObj,1)
print(student1.score)
student2 = stru_stru.StudentArray_getitem(res.studentObj,2)
print(student2.score)

