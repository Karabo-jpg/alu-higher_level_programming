#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};

// Log initial state
console.log(`${myObject.type} + ${myObject.value}`);

// Update value and log updated state
myObject.value = 89;
console.log(`${myObject.type} + ${myObject.value}`);

