// Fizz Buzz
// Write a function fizzBuzz that takes an array of numbers and replaces any number divisible by three with the word "fizz" and any number divisible by five with the word "buzz". If a number is divisible by both three and five, replace it with "fizzbuzz"
// Once the appropriate numbers are replaced, return a concatenated string with only the words "fizz" or "buzz" included.

const numbers = [1, 3, 5, 9, 11, 12, 20];

function fizzBuzz(numbers) {
    let str = "";
    for(let i = 0; i < numbers.length; i++) {
        const number = numbers[i];
        if (number % 3 === 0) {
            str += "fizz";
        }  
        if (number % 5 === 0) {
            str += "buzz";
        } 
    }
    return str;
}

fizzBuzz(numbers); // returns "fizzbuzzfizzfizzbuzz"