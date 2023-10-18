// Sort ascending
function sortUp(array) {
    array.sort((a,b) => a-b);
}

// Sort descending
function sortDown(array) {
    array.sort((a,b) => b - a);
}

// Sort strings ascending
function sortStringsUp(array) {
    array.sort((a,b) => a.localeCompare(b));
}

// Sort strings descending
function sortStringsDown(array) {
    array.sort((a,b) => b.localeCompare(a));
}

// Sort by multiple properties
const students = [
    { id: 1, graduated: true, grade: 86 },
    { id: 2, graduated: false, grade: 96 },
    { id: 3, graduated: false, grade: 78 },
    { id: 4, graduated: true, grade: 96 },
];

    // sort by graduated then highest grades
    function sortStudents(students) {
        students.sort((a,b) =>{
            if (a.graduated && !b.graduated){
                return -1;
            }
            else if (!a.graduated && b.graduated){
                return 1;
            }
            return b.grade - a.grade;
        })
    }

    // Sort by enumeration (e.g. month)
    const MONTHS = [
        'JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN',
        'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'
    ];
    
    function sortByMonth(events) {
        events.sort((a, b) => MONTHS.indexOf(a.month) - MONTHS.indexOf(b.month));
    }