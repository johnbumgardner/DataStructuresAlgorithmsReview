#include <stdio.h>
#include <limits.h>
#include <stdint.h>
int main() {
	unsigned int number;
	unsigned int rotations;
	scanf("%d", &number);
	scanf("%d", &rotations); 

	unsigned int mask = ~(-1 << rotations);
	unsigned int temp = number & mask;
	number >>= rotations;
	number += (temp << (32 - rotations));
	printf("%d\n", number );
}