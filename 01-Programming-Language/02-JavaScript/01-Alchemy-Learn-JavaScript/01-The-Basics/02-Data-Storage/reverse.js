// Reverse
// Write a function reverse that takes a string as an argument and returns a string with all the letters reversed.
// For example, reverse("cat") would return the string "tac".

function reverse(string) {
    let newStr = "";
    let j = string.length - 1;

    for (let i = 0; i < string.length; i++){
        newStr += string[j];
        j--;
    }
    return newStr;
}