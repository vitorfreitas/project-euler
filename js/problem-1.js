function range(min, max) {
  let arr = [];
  for (let i = min; i < max; i++) {
    arr.push(i);
  }
  return arr;
}

function solve(arr) {
  const result = arr.reduce((acc, cur) => {
    if (cur % 3 === 0 || cur % 5 === 0) {
      return (acc += cur);
    }
    return acc;
  }, 0);
  return result;
}

console.log(solve(range(1, 1000)));
