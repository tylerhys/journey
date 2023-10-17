function isEven(num) {
    let check = num % 2;

    if (check === 0){
        return true;
    }
    else {
        return false;
    }
}

console.log( isEven(1) ); // false
console.log( isEven(4) ); // true