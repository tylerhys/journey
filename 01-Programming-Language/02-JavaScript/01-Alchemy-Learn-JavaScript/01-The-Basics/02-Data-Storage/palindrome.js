// Write a function isPalindrome that takes a word string and returns true if the word is a palindrome or false if it is not.
// A palindrome is a word that is spelled the same forwards as it is backwards.

function isPalindrome(string) {
    let j = string.length - 1;

    for (i = 0; i < string.length; i++){
        if (string[i] !== string[j]){
            return false;
        }
        j--;
    }
    return true;
}