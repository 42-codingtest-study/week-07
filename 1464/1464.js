const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");

solution(input);
function solution(input) {
  const s = input[0];
  let ans = [];

  for (const c of s) {
    if (ans.length === 0) ans.push(c);
    else if (ans[0] < c) ans.push(c);
    else ans.unshift(c);
  }

  console.log(ans.join(""));
}
