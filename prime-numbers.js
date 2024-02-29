/*
Create a JavaScript program that outputs all the prime numbers between 1 and upper limit. 
Enable this program to run from the command line and automatically pass in the upper limit 
from the command line.
*/

// primeNumbers.js

function isPrime(num) {
  if (num <= 1) return false;
  for (let i = 2; i <= Math.sqrt(num); i++) {
    if (num % i === 0) return false;
  }
  return true;
}

function generatePrimes(upperLimit) {
  const primes = [];
  for (let i = 2; i <= upperLimit; i++) {
    if (isPrime(i)) {
      primes.push(i);
    }
  }
  return primes;
}

const upperLimit = parseInt(process.argv[2]);

if (isNaN(upperLimit) || upperLimit < 1) {
  console.error("Please provide a valid positive integer as the upper limit.");
} else {
  const primeNumbers = generatePrimes(upperLimit);
  console.log(`Prime numbers between 1 and ${upperLimit}:`);
  console.log(primeNumbers.join(", "));
}
