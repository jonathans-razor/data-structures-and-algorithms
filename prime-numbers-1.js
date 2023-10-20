// GPT 3.5 Prompt used: Create a javascript program that prints out the prime numbers between 1 and 100.
function isPrime(num) {
  if (num <= 1) return false;
  if (num <= 3) return true;
  
  if (num % 2 === 0 || num % 3 === 0) return false;
  
  for (let i = 5; i * i <= num; i += 6) {
    if (num % i === 0 || num % (i + 2) === 0) return false;
  }
  
  return true;
}

function printPrimeNumbers() {
  for (let i = 1; i <= 100; i++) {
    if (isPrime(i)) {
      console.log(i);
    }
  }
}

printPrimeNumbers();