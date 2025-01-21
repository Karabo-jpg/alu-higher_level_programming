#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};

console.log(`${myObject.type} + ${myObject.value}`);
myObject.value = 89;
console.log(`${myObject.type} + ${myObject.value}`);
