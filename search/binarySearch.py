def binarySearch(sortedArr, val):
	start  = 0
	end = len(sortedArr) - 1
	middle = end//2

	while(sortedArr[middle] != val):
		if(start > end):
			return -1 

		if(sortedArr[middle] > val):
			end = middle - 1
		else:
			start = middle + 1
	
		middle = (start+end)//2

	return middle


def main():
	result = binarySearch([-2, 0, 1, 2, 3, 4, 5, 6], 1)

	print(result)


main()
