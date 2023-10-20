function calculateBowlingScore(rolls) {
  let score = 0;
  let frameIndex = 0;

  for (let frame = 0; frame < 10; frame++) {
    if (isStrike(frameIndex)) {
      score += 10 + strikeBonus(frameIndex);
      frameIndex++;
    } else if (isSpare(frameIndex)) {
      score += 10 + spareBonus(frameIndex);
      frameIndex += 2;
    } else {
      score += sumOfPinsInFrame(frameIndex);
      frameIndex += 2;
    }
  }

  return score;

  function isStrike(frameIndex) {
    return rolls[frameIndex] === 10;
  }

  function isSpare(frameIndex) {
    return rolls[frameIndex] + rolls[frameIndex + 1] === 10;
  }

  function strikeBonus(frameIndex) {
    return rolls[frameIndex + 1] + rolls[frameIndex + 2];
  }

  function spareBonus(frameIndex) {
    return rolls[frameIndex + 2];
  }

  function sumOfPinsInFrame(frameIndex) {
    return rolls[frameIndex] + rolls[frameIndex + 1];
  }
}

// Example usage:
const rolls = [10, 7, 3, 5, 2, 5, 8, 0, 10, 10, 10, 6, 3, 10, 8, 2, 9];
const totalScore = calculateBowlingScore(rolls);
console.log("Total Score:", totalScore);