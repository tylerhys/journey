const Shape = require('./exampleShape');

function Rectangle(x, y, height, width) {
    Shape.call(this, x, y);
    this.height = height;
    this.width = width;
}


Rectangle.prototype = Object.create(Shape.prototype);

Rectangle.prototype.flip = function(){
    let temp = this.height;
    this.height = this.width;
    this.width = temp;
}

// Test
const rect = new Rectangle(0, 0, 20, 40);

console.log(rect.x, rect.y); // 0, 0
console.log(rect.height, rect.width); // 20, 40

rect.flip();

console.log(rect.height, rect.width); // 40, 20