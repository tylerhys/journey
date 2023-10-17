// Write a function countElements that takes in an array and returns an object a count of each element in the array.

const elements = ["e", "k", "e", "z", "i", "z"];

function countElements(elements) {
    let count = {};
    for (let i = 0; i < elements.length; i++){
        if (!count[elements[i]]){
            count[elements[i]] = 1;
        }
        else{
            count[elements[i]]++
        }
    }
    return count;
}

countElements(elements); // returns {e: 2, k: 1, z: 2, i: 1}