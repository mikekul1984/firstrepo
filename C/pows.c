#include<stdio.h>
#include<math.h>

int main (void)
{
	printf ("Args: 2.6 and 3.45\n");
	printf ("powf : %.20f\n", powf (2.6, 3.45));
	printf ("pow : %.20f\n", pow (2.6, 3.45));
	printf ("powl : %.20Lf\n", powl (2.6, 3.45));

	return 0;
}
