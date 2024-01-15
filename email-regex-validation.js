const email = process.argv[2];
const regex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
const isValidEmail = regex.test(email);
console.log(isValidEmail);