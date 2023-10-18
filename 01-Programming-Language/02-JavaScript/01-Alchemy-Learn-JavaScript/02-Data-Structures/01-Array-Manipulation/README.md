## **Topic Summary: Array Sort**
Array Sort
```
array.sort((a,b) => a-b);
```
Compare Strings
```
'a'.localeCompare('a'); // 0
'a'.localeCompare('b'); // -1
"apple".localeCompare("abcd"); // 1
```
indexOf
```
Array.prototype.indexOf(element);

const MONTHS = ['JAN', 'FEB', 'MAR'];

console.log( MONTHS.indexOf('JAN') ); // 0
console.log( MONTHS.indexOf('MAR') ); // 2
console.log(MONTHS.indexOf('go fish')); // -1
```

## **Topic Summary: Array Map**
Map Function
```
array.map(function(x) {
    return x;
})
```
Mapping Over Objects
```
array.map(function(el, i) {
    console.log(i)
});
```
## **Topic Summary: Array Filter**
Filter Function
```
array.filter((function(el) {
    return (condition);
}))
```
Filter by Index
```
//first arg is element, second arg is position
array.filter(function(el, i) {
    console.log(el, i);
});
```
## **Topic Summary: Array Reduce**
Reduce Function
```
array.reduce((accumulator,currentValue)=>{
    return;
});
```
Index
```
['a','b','c'].reduce((accumulator, currentValue, index) => {
    function; 
});
```
Ternary Operator
```
//if else
(x > y ? x : y)
```
## **More Info**
**localeCompare Documentation:** [Link](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/localeCompare)
**Ternary Operators Documentation:** [Link](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_Operator)