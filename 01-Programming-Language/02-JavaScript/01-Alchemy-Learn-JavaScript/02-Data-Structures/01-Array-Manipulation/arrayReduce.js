// Sum of arrays using reduce
// [1,2,3,4,5] => 15
function sum(numbers) {
    return numbers.reduce((accumulator, currentValue) => {
        return accumulator + currentValue// <-- sum the numbers here!
    });
}

// Largest +ve Value
function largest(numbers) {
    return numbers.reduce((accumulator, currentValue) => {
        return accumulator > currentValue ? accumulator : currentValue// <-- determine largest value
    },1); // <-- initial value
}

// Remove Dups
function removeDuplicates(numbers) {
    return numbers.reduce((accumulator, currentValue) => {
        // TODO: reduce logic
        if (accumulator.indexOf(currentValue) === -1){
            accumulator.push(currentValue);
        } return accumulator;
    }, []/* TODO: add initial value */ );
}

// Group with Reduce
        // Input
        const input =
        [
            { food: 'apple', type: 'fruit' }, 
            { food: 'orange', type: 'fruit' }, 
            { food: 'carrot', type: 'vegetable' }
        ]

        // Output
        const output = 
        { 
            fruits: ['orange', 'apple'], 
            vegetable: ['carrot'] 
        }

function group(foods) {
    return foods.reduce((accumulator, currentValue) => {
        accumulator[currentValue.type] = accumulator[currentValue.type] || []
        accumulator[currentValue.type].push(currentValue.food);
        return accumulator;
    }, {});
}

// Is Unique
function allUnique(numbers) {
    return numbers.reduce((accumulator, currentValue, index) => {
        if (!accumulator) return false;
        return numbers.indexOf(currentValue) === index;
    }, true);
}