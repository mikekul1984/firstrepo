#include <stdio.h>

unsigned long long factorial(unsigned long long n)
{
	if (n == 0) {
		return 1;
	} else {
		return n * factorial(n-1);
	}
}

int main(void)
{
	int n;
	for (n = 0; n <= 16; n++) {
		printf("%i! = %lld\n", n, factorial(n));
	}

	return 0;
}
