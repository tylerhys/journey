// Filter less than five
function lessThanFive(array) {
    return array.filter((el) => {
        return el < 5;
    });
}

// Filter true
function onlyTrue(array) {
    return array.filter(el =>{
        return el === true;
    })
}

// Filter strings (length <=3)
function shortStrings(array) {
    return array.filter(el => {
        return el.length <= 3;
    })
}

// Filter Objects (grades >= 90)
const students = [
    { name: 'David', grade: 90 }, 
    { name: 'Daisy', grade: 100 },
    { name: 'Darcie', grade: 80 }
];

function topStudents(array) {
    return array.filter(el => {
        return el.grade >= 90;
    })
}

// Filter by Index
function firstThree(array) {
    return array.filter((x,i) => {
        return i < 3;
    })
}

// Filter unique
function unique(array) {
    return array.filter((el, i)=>{
        return i === array.indexOf(el);
    }
    )
}