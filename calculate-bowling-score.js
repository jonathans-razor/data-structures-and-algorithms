// Calculate bowling score based on command line input.
const readline = require("readline");

function calculateScore(frames) {
  let score = 0;
  let frameIndex = 0;

  for (let i = 0; i < 10; i++) {
    if (frames[frameIndex] === "X") {
      score += 10 + getStrikeBonus(frameIndex, frames);
      frameIndex++;
    } else if (frames[frameIndex + 1] === "/") {
      score += 10 + getSpareBonus(frameIndex, frames);
      frameIndex += 2;
    } else {
      score += getFrameScore(frameIndex, frames);
      frameIndex += 2;
    }
  }

  return score;
}

function getStrikeBonus(frameIndex, frames) {
  return (
    getFrameScore(frameIndex + 1, frames) +
    getFrameScore(frameIndex + 2, frames)
  );
}

function getSpareBonus(frameIndex, frames) {
  return getFrameScore(frameIndex + 2, frames);
}

function getFrameScore(frameIndex, frames) {
  let score = getRollScore(frames[frameIndex]);

  if (frames[frameIndex + 1]) {
    score += getRollScore(frames[frameIndex + 1]);
  }

  return score;
}

function getRollScore(roll) {
  if (roll === "X" || roll === "/") {
    return 10;
  } else if (roll === "-") {
    return 0;
  } else {
    return parseInt(roll);
  }
}


const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.question("Enter the rolls in your game of bowling: ", (answer) => {
  const frames = answer.split(",");
  const score = calculateScore(frames);
  console.log(`The score of your game is ${score}.`);
  rl.close();
});