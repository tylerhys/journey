function checkNumber(num) {
    if (num > 0) {
        return "positive"
    }
    else if (num < 0) {
        return "negative"
    }
    else if (num === 0){
        return "zero";
    }
}

console.log( checkNumber( -3 ) ); // negative
console.log( checkNumber( 0 ) ); // zero
console.log( checkNumber( 2 ) ); // positive