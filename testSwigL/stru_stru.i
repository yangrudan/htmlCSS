/* File : stru_stru.i */
%module stru_stru
%inline %{
/*Put headers and other declarations here */
    struct Student{
        int age;
        int score;
    };

    struct School{
        int class_num;
        struct Student studentObj[10];
    };

    struct School create();
%}

%include carrays.i
%array_functions(struct Student, StudentArray);
%array_class(struct Student, StudentClass)
extern struct School create();