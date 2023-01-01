const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");

solution(input);
function solution(input) {
  const N = input[0] * 1;
  const balloons = input[1].split(" ").map((e) => e * 1);
  const answer = [];
  const visited = new Array(N).fill(false);
  let curr = 0;
  while (true) {
    answer.push(curr + 1);
    if (answer.length === N) break;
    visited[curr] = true;
    let move = balloons[curr];

    if (move > 0) {
      while (move > 0) {
        curr = (curr + 1) % N;
        if (!visited[curr]) {
          move--;
        }
      }
    } else {
      move *= -1;
      while (move > 0) {
        curr = curr === 0 ? N - 1 : curr - 1;
        if (!visited[curr]) {
          move--;
        }
      }
    }
  }
  console.log(answer.join(" "));
}
