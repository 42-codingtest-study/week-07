const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");

solution(input);

function solution(input) {
  const [n, w, L] = input[0].split(" ").map((e) => e * 1);
  // n 개의 트럭 , 다리길이 w, 다리의 최대하중 L
  const truck = input[1].split(" ").map((e) => e * 1);
  const deque = new Array(w).fill(0);
  let answer = 0;
  //   console.log(deque, truck, answer);
  while (true) {
    if (deque.reduce((a, b) => a + b, -deque[0]) + truck[0] > L) {
      deque.shift();
      deque.push(0);
      answer += 1;
    } else {
      deque.shift();
      temp = truck.shift();
      deque.push(temp === undefined ? 0 : temp);
      answer += 1;
    }
    if (deque.reduce((a, b) => a + b, 0) === 0) break;

    // console.log(deque, truck, answer);
  }
  console.log(answer);
}
