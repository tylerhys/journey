// Your Goal: Count the C's
// The function countC takes a string str as its only argument.
// This function should return the number of c's found in the string. It must count both lower-case c and upper-case C.

function countC(str) {
    let count = 0;
    for (i = 0; i < str.length;i++){
        if (str[i].toUpperCase() === "C"){
            count++;
        }
    }
    return count;
}