function countNumbersWithRepeatedDigits(N) {
  let count = 0;
  for (let i = 1; i <= N; i++) {
    if (hasRepeatedDigits(i)) {
      count++;
    }
  }
  return count;
}

function hasRepeatedDigits(n) {
  let digits = new Set();
  while (n > 0) {
    let digit = n % 10;
    if (digits.has(digit)) {
      return true;
    }
    digits.add(digit);
    n = Math.floor(n / 10);
  }
  return false;
}

let N = parseInt(process.argv[2]);
console.log(countNumbersWithRepeatedDigits(N));