#include <stdio.h> 
#include <stdlib.h> 
int main(int argc, char *argv[]){ 
        int day, month, year; 
        int n = 0; 

        if (argc > 2) { 
                day = atoi(argv[1]); 
                month = atoi(argv[2]); 
                year = atoi(argv[3]); 
        } else { 
                printf("Type date: day month year.\n"); 
                scanf("%d%d%d", &day, &month, &year); 
        } 

        switch (month) { 
                case 1: n += 31; 
                case 2: n += (year % 400 == 0 ||(year % 4 == 0 &&
                        year % 100 != 0)) ? 29 : 28; 
                case 3: n += 31; 
                case 4:  n += 30; 
                case 5:  n += 31; 
                case 6:  n += 30; 
                case 7:  n += 31; 
                case 8:  n += 31; 
                case 9:  n += 30; 
                case 10:  n += 31; 
                case 11:  n += 30; 
                case 12:  n += 31; 
        } 
        n -= day; 
        printf("%d days before New Year's day\n", n); 
        return 0; 
}
