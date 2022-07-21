const binarySearch = (arr, val) => {
  let start = 0;
  let end = arr.length - 1;
  let middle = Math.floor((start + end) / 2);

  while (arr[middle] !== val) {
    if (start > end) return -1;

    if (val > arr[middle]) {
      start = middle + 1;
    } else {
      end = middle - 1;
    }

    middle = Math.floor((start + end) / 2);
  }

  return middle;
};

const binarySearch2 = (sortedArr, val) => {};

const result = binarySearch([-2, 0, 1, 2, 3, 4, 5, 6], 1);

console.log(result);
