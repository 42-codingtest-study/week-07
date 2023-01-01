const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");

solution(input);

function solution(input) {
  const [A, B, C] = input
    .shift()
    .split(" ")
    .map((e) => e * 1);
  const normal_menu = new Map();
  const special_menu = new Map();
  const service_menu = [];
  let order = [];
  let normal_price = 0;
  let special_price = 0;
  let service_num = 0;
  for (let i = 0; i < A; i++) {
    const [key, value] = input.shift().split(" ");
    normal_menu.set(key, value * 1);
  }
  for (let i = 0; i < B; i++) {
    const [key, value] = input.shift().split(" ");
    special_menu.set(key, value * 1);
  }
  for (let i = 0; i < C; i++) {
    service_menu.push(input.shift());
  }
  input.shift();
  order = input;
  let price = 0;
  for (menu of order) {
    price = normal_menu.get(menu);
    if (price !== undefined) {
      normal_price += price;
      continue;
    }
    price = special_menu.get(menu);
    if (price !== undefined) {
      special_price += price;
      continue;
    }
    if (service_menu.indexOf(menu) > -1) service_num += 1;
  }
  let answer = "Okay";
  if (normal_price < 20000 && special_price > 0) answer = "No";
  else {
    if (normal_price + special_price < 50000 && service_num > 0) answer = "No";
    else if (service_num > 1) answer = "No";
  }
  console.log(answer);
  console.log(normal_price, special_price, service_num);
}
