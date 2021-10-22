#include <stdio.h>
#define PERSON_NUM 5

struct person_dt{
    char name[20];
    char sex;
    int age;
    double height;
    double weight;
};


int main(void){
    
    struct person_dt p[PERSON_NUM]={
        {"Bob", 'M', 19, 165.4, 72.5},
        {"Alice", 'F', 19, 161.7, 44.2},
        {"Tom", 'M', 20, 175.2, 66.3},
        {"Stefany",  'F', 18, 159.3, 48.5},
        {"Leonardo", 'M', 19, 172.8, 67.2}
    };

    for(int i=0; i<PERSON_NUM; i++){
        printf("%s %c %d %.1f %.1f\n", p[i].name, p[i].sex, p[i].age, p[i].height, p[i].weight);
    }

    return 0;
}
