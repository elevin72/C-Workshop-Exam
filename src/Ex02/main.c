#include <stdio.h>
#include <malloc.h>
#include "greeting.h"

int main(int argc, char** argv) {
	char* message = greeting();
	printf(message);
	free(message);
	return 0;
}