#include <stdio.h>
#include <unistd.h>

int main(int argc, char *argv[]){
	FILE *secret = fopen("/root/root-me-challenges/app-systeme/ch5/.passwd", "rt");
	char buffer[32];
	fgets(buffer, sizeof(buffer), secret);
	printf(argv[1]);

	printf("\n");
	printf("%s\n",buffer);
	printf("%x\n",buffer);
	printf("%p\n",buffer);
	fclose(secret);
	return 0;
}
