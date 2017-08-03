#include <stdlib.h>
int foo(int a, int b, int c);

int main()
{
	int i = 0;

	i =  foo(1,2,3);

	return 0;
}

int foo(int a, int b, int c)
{
	return a;
}
