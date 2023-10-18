// Factorial
function factorial(n) {
    if(n === 1){
        return 1;
    }
    return n * factorial(n -1)
}

// Sumation
function summation(n) {
    if(n < 1) return 0;

    return n + summation(n - 1);
}

// Walk a node (return last node)
function walk(node) {
    if (node.next === undefined){
        return node;
    } return walk(node.next);
}