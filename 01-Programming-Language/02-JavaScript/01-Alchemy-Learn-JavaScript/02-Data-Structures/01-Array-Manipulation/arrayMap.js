// Plus One
function plusOne(arr) {
    return arr.map(x => x+1);
}

//Square Root
function squareRoot(arr) {
    return arr.map(x => Math.sqrt(x));
}

// Mapping Over Objects (add score to first 3 players)
function addScore(players) {
    return players.map((x,i) => {
        if(i < 3){
            x.score += 10;
        }
        return x;
    });
}