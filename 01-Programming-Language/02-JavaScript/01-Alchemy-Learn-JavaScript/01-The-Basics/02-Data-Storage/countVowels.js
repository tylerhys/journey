// Write a function countVowels that takes in a string and counts how many vowels there are in the word. Vowels include: "a", "e", "i", "o", and "u".
// Handle lowercase and uppercase vowels.

function countVowels(str) {
    let count = 0;

    for (let i = 0; i < str.length; i++){
        if(["A","E","I","O","U"].includes(str[i].toUpperCase())){
            count++;
        }
    }

    return count;
}