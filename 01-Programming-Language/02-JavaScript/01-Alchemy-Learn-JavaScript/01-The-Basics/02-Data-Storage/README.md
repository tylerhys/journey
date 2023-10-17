## **Topic Summary: String Manipulation**
Looking up Characters
```
"Hello".charAt(1); // e
"Hello"[1]; // e
```
Compare Strings
```
( 'a' === 'a' ); // true
( 'a' !== 'A' ); // false
( 'a' > 'b' ); // false
( 'a' < 'b' ); // true
```
String Functions
```
string.toUpperCase();
string.toLowerCase();
string.length;
"Hello".indexOf("e"); // 1

```
String Looping
```
const string = "Hello";
for(let i = 0; i < string.length; i++) {
    console.log(string[i]);
}
```
Slicing String
```
"The 40 Thieves".slice(4,8); // 40 T
"Please Slice Me".slice(7); // Slice Me
"the apple".slice(-5); // apple
"the apple".slice(-5, -2); // app
```

## **Topic Summary: Arrays**
Arrays
```
const numbers = [1, 2, 3, 4, 5];
const nested = [[1, 2, [1, 2]], 2];
const element = array[0];
```
Add Element
```
const newArray = [];
newArray.push(element);
```
Remove Element
```
const newArray = [];
newArray.splice(i,1); // first arg is starting index, sec arg is num of elements, hence use decreasing loop
```
Contains Element
```
array.indexOf(element) >= 0 // true if exists
```

## **Topic Summary: Objects**
Objects
```
const team = {
    name: "Mets",
    wins: 86,
    inPlayoffs: false,
};

// Array of objects
const orders = [
    { pizzas: 3 },
    { pizzas: 5 },
    { pizzas: 10 }
];
```
Retrieve Value
```
team.name;
team['name'];
```
Enumeration
```
//See orderTypes.js (enumeration) and numberOfPizzas.js
```
Get All Keys in Objects
```
const object = { a: 1, b: 2, c: 3 } 
for(let key in object) {
    console.log(key);
}
```
Remove Keys
```
const person = { 
    name: "Bob"
}

delete person.name;
```
## **More Info**
**String Documentation:** [Link](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String)
**Array Documentation:** [Link](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
**Objects Documentation:** [Link](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object)