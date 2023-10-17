// Player Hand Score
// The function playerHandScore that takes in a string of face cards (Jack, Queen, and King only) and returns the total score of the players hand.
// The cards are represented by the first letter in the name of the card:
// A "K" is 4 points
// A "Q" is 3 points
// A "J" is 2 points

function playerHandScore(hand) {
    const card = {
        "K" : 4,
        "Q" : 3,
        "J" : 2,
    }

    let score = 0;

    for (let i = 0; i < hand.length; i++){
        score = score + card[hand[i]];
    }
    return score;
}

console.log( playerHandScore("K") ); // 4
console.log( playerHandScore("KJ") ); // 6
console.log( playerHandScore("KQQ") ); // 10 