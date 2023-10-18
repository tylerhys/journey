## **Topic Summary: This Keyword**
Using This
```
function thisName() {
    return this.name;
}

const name = thisName.call({ name: 'Ted' }); 

console.log(name); // Ted
```
Bind
```
// Bind Arguments
function add(x, y) {
    return x + y;
}
const addTwo = add.bind(null, 2);

console.log( addTwo(2) ); // 4
console.log( addTwo(10) ); // 12

// Bind Functions
function thisName() {
    return this.name;
}

const newFunction = thisName.bind({ name: 'Ted' }); 

console.log(newFunction()); // Ted
```
Fix Unbound Functions
```
// Problem Code
function addYear() {
    setTimeout(function() {
        this.age++;
    }, YEAR);
}

// Closure
function addYear() {
    const that = this; // fix
    setTimeout(function() {
        that.age++;
    }, YEAR);
}

// Bind
function addYear() {
    setTimeout(function() {
        this.age++;
    }.bind(this), 1); // fix
}

// Arrow Syntax
function addYear() {
    setTimeout(() => {
        this.age++;
    }, YEAR);
}
```
## **Topic Summary: Prototype**
Prototype Chain
```
function Car(make, model) {
    this.make = make;
    this.model = model;
}

const car = new Car('Toyota', 'Camry');
const car2 = new Car('Honda', 'Civic');

console.log(car.make) // Toyota
console.log(car2.model) // Civic
```
Examples of Usage
```
// Refer to exampleCircle.js, exampleShape.js and exampleRectangle.js
```
## **Topic Summary: Classes**
Create a class
```
class Hero {
    constructor() {
        this.health = 50;
    }
}
```
Adding Methods
```
class Hero {
    constructor(health) {
        this.health = health;
    }

    takeDamage(damage){
        this.health -= damage;
    }
}
```
Sub Classes
```
const Hero = require('./Hero');

class Warrior extends Hero {
    
}
```
Super //calls constructor/methods from parent class
```
const Hero = require('./Hero');

class Warrior extends Hero {
    constructor(health){
        super(health); // Calls Constructor
        this.rage = 0;
    }
    takeDamage(damage){
        super.takeDamage(damage); // Calls Method
        this.rage += 1;
    }
}
```
## **More Info**
**Arrow Function Documentation:** [Link](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)