function maxSum(num) {
    let newNum = 0;
    let sum = 0;

    while (newNum <= num){
        sum = sum + newNum;
        newNum = newNum + 1;
    }

    return sum;
}
