function niceRegularBox(lines) {
  let maxChar = [];
  let max = " ";
  for (let maxArray = 0; maxArray < lines.length - 1; maxArray++) {
    maxChar[maxArray] = lines[maxArray];
      if (maxArray > 0) {
        if (maxChar[maxArray - 1].length <= maxChar[maxArray].length) {
          max = maxChar[maxArray].length;
        }
    }
  }
  console.log ("+" + "-".repeat(max+2) + "+");

}
