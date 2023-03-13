/*
create nested struct array for used in python
*/


struct Student{
    int age;
    int score;
};

struct School{
    int class_num;
    struct Student studentObj[10];
};

/*@brief: return a School Obj*/
struct School create()
{
    struct School ret;
    ret.class_num = 3;
    for(int i =0; i<10; i++)
    {
        ret.studentObj[i].score = 100;
    }
    return ret;
}