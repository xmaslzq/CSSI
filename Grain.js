function square(noSquare) {
  let total = 0;
  for (let i = 0; i <= noSquare - 1; i++) {
    total = total + 2**i;
  }
  return total;
}
