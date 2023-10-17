// Sum Together
// Write a function sumTogether that takes two arrays of numbers and returns a single array with the sum of each corresponding index value.
// Assume both arrays are the same length.

const arr1 = [1, 2, 3];
const arr2 = [3, 4, 5];

function sumTogether(arr1, arr2) {
    let newArr = [];

    for(let i = 0; i < arr1.length; i++){
        newArr[i] = arr1[i] + arr2[i];
    }
    return newArr;
}

sumTogether(arr1, arr2); // returns [4, 6, 8];