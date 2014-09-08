#include<stdio.h>
#include<math.h>
void func1(int x1)
{
	int i,b;
	long c = 0;
	for(i=0;x1 >0;i++)
	{
		b = x1 % 2;
		x1 = (x1 - b)/2;
		c += b * pow(10,i);
	}
	printf("\nchislo: %d", c);
}

int  main()
{
	int a;
	printf("Enter a number:");
	scanf("%d", &a);
	func1(a);
	return 0;
}
