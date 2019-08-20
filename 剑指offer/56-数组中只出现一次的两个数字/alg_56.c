#include <stdio.h>
#include <stdlib.h>

int FindFirstBitIs1(int num) {
	int indexBit = 0;
	while (((num & 1)==0) && (indexBit < 8 * sizeof(int))) {
		num = num >> 1;  // 找到最后面的那个1
		++ indexBit;
	}

	return indexBit;
}

int IsBit1(int num, int indexBit) {
	num = num >> indexBit;
	return (num & 1);
}

void FindNumsAppearOnce(int data[], int length, int* num1, int* num2) {
	if (data == NULL || length < 2) {
		return;
	}

	int resultExclusiveOR = 0;
	for (int i=0; i<length; i++) {
		resultExclusiveOR ^= data[i];
	}

	int indexOf1 = FindFirstBitIs1(resultExclusiveOR);

	*num1 = *num2 = 0;
	for (int j=0; j<length; j++) {
		if(IsBit1(data[j], indexOf1)) {
			// printf("before: %d, %d\n", *num1, data[j]);
			*num1 ^= data[j];
			// printf("num1: %d\n", *num1);
		}
		else {
			*num2 ^= data[j];
		}
	}
}



int main(int argc, char const *argv[])
{
	int lst[] = {2, 4, 3, 6, 3, 2, 5, 5};
	int length = sizeof(lst) / sizeof(int);
	int num1;
	int num2;
	FindNumsAppearOnce(lst, length, &num1, &num2);
	printf("%d, %d\n", num1, num2);
	return 0;
}