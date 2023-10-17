// Your Goal: Halve 'em! 
// The function halfValue takes an array of numbers. It should return a new array with all the original values halved.
// Odd numbers should be rounded up to the nearest whole number.

function halfValue(numbers) {
    const newArr = [];

    for (let i = 0; i < numbers.length; i++){
        newArr[i] = Math.round(numbers[i] / 2);
    }
    return newArr;
}