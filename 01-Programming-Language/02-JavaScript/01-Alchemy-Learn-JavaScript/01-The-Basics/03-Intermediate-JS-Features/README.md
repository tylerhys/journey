## **Topic Summary: Logical Operators**
Logical Operators
```
// OR aka Default
x || y;

// AND aka Guard
x && y

// NOT
!x;
```

## **Topic Summary: Errors**
Throw Error
```
throw new Error("Something went wrong!");
```
Catch Error
```
function catchError(fn) {
    try{
        fn();
    }
    catch(ex){
        return ex;
    }
    return false;
}
```

## **Topic Summary: Type Conversion**
Check Type
```
console.log( typeof 1 ); // number
console.log( typeof "1" ); // string
console.log( typeof {} ); // object
```

String to Number
```
Number(string);
parseInt(string);
parseFloat(string);

```
To String
```
a.toString();
String(a);
(123 + "");
```
Loose Equals
```
("2" === 2); // false
("2" == 2); // true
```
JSON
```
const itemJSON = `{
    "type": "food",
    "edible": true,
    "quantity": 2
}`
```
JSON to Object
```
const item = JSON.parse(itemJSON);
```
Object to JSON
```
function toJSON(obj) {
    return JSON.stringify(obj);
}
```
Destructuring
```
const { a, b } = obj;
const [a, b] = arr;
```
Rest Parameters
```
function log(...args) {
    console.log(args);
}

log(1, 2, 3, 4, 5); // [1, 2, 3, 4, 5]
```
Spread Arguments
```
const numbers = [1, 2, 3];

function add(a, b, c) {
  return a + b + c;
}

const sum = add(...numbers);
```
## **More Info**
**Common System Errors:** [Link](https://nodejs.org/api/errors.html#errors_common_system_errors)
**JSON Documentation:** [Link](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON)
**Destructuring Documentation:** [Link](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment)