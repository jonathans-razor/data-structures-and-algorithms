function reverseString(str: string): string {
    return str.split("").reverse().join("");
}

const inputString = process.argv[2];
const reversedString = reverseString(inputString);

console.log(`The reversed string of "${inputString}" is "${reversedString}".`);