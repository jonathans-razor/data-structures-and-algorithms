var phoneRegex = /^\d{3}-\d{3}-\d{4}$/;
console.log(phoneRegex.test("123-456-7890")); // true
console.log(phoneRegex.test("123-456-789x")); // false