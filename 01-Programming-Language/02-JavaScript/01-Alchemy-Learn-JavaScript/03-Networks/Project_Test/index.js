const { faker } = require('@faker-js/faker');
const name = faker.person.fullName();
const message = `Hello, ${name}!`;
console.log(message);