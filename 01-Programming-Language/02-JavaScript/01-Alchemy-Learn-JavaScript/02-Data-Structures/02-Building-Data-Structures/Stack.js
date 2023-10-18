const { MAX_STACK_SIZE } = require('./config');

class Stack {
    constructor() {
        this.items = [];
    }
    push(item) {
        if (this.items.length === MAX_STACK_SIZE) {
            throw new Error("Stack Overflow!");
        }
        this.items.push(item);
    }
    pop() {
        if (this.items.length === 0) {
            throw new Error("Stack Underflow");
        }
        return this.items.pop();
    }
    isEmpty() {
       if (this.items.length === 0) {
           return true;
       }
    }
    peek() {
        return this.items[this.items.length-1];

    }
}