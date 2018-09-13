
#include <stdio.h>

int main()
{
	int a, b, c, avg;
	printf("Choose three numbers: ");
	scanf("%d %d %d", &a, &b, &c);
	avg = ((a+b+c)/3);
	printf("The average of %d, %d, & %d is %d\n", a, b, c, avg);
	return 0;
}
