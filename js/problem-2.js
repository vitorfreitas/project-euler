function fib(limit) {
  const arr = [1, 2];
  while (arr.length < limit) {
    const last = arr[arr.length - 1];
    const lastButOne = arr[arr.length - 2];
    arr.push(last + lastButOne);
  }
  return arr;
}

const result = fib(4000000);

console.log(result[result.length - 1]);
