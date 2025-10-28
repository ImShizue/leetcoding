#include <stdio.h>

int jump(int *nums, int numSize)
{
	if (numSize == 1) return 0;

	int j = 0;
	int e = 0;
	int f = 0;
	
	for (int i = 0; i < numSize - 1; i++) {
		//printf("---\n");
		if (i + nums[i] > f) {
			f = (i + nums[i]);
		}


		if (i == e) {
			j++;
			e = f;
			//printf("j = %d\nf= %d\n", j,f);
		}
	}
	return j;
}


int main(void)
{
	int nums[3] = {3,2,1};
	int numSize = 3;
	printf("jump : %d\n",jump(nums, numSize));
	return 0;
}