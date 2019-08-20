#include <stdio.h>
#include <stdlib.h>


/*
	使用两次二分查找找到第一个和最后一个K
*/


int getFirstK(int* data, int k, int start, int end) {
	if (start > end){
		return -1;
	}

	int middleIndex = (start + end) / 2;
	int middleData = data[middleIndex];

	if (middleData == k) {
		if ((middleIndex > 0 && data[middleIndex - 1] != k) || middleIndex == 0) {
			return middleIndex;
		}
		else if (middleIndex > 0 && data[middleIndex - 1] == k) {
			end = middleIndex - 1;
		}
	}
	else if (middleData > k) {
		end = middleIndex - 1;
	}
	else {
		start = middleIndex + 1;
	}
	return getFirstK(data, k, start, end);
}

int getLastK(int* data, int k, int start, int end) {
	if (start > end) {
		return -1;
	}

	int middleIndex = (start + end) / 2;
	int middleData = data[middleIndex];

	if (middleData == k) {
		if ((middleIndex < end && data[middleIndex + 1] != k) || middleIndex == end) {
			return middleIndex;
		}
		else if (middleIndex < end && data[middleIndex + 1] == k) {
			start = middleIndex + 1;
		}
	}
	else if (middleData > k) {
		end = middleIndex - 1;
	}
	else {
		start = middleIndex + 1;
	}
	return getLastK(data, k, start, end);
}

int getNumberOfK(int* data, int k, int length)
{
	int number = 0;

	if (data != NULL && length > 0) {
		int first = getFirstK(data, k, 0, length-1);
		int last = getLastK(data, k, 0, length-1);

		if (first != -1 && last != -1) {
			number = last - first + 1;
		}
	}
	return number;
}

int main() {
  int data[] = {1, 2, 3, 3, 3, 3, 4, 5};
  int length = sizeof(data) / sizeof(int);
  int number = getNumberOfK(data, 3, length);
  printf("%d\n", number);
  return 0;
}