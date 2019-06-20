/*
let macbeth = "Tomorrow and tomorrow and tomorrow";
let richard = "Now is the winter of our discontent";
console.log("I love shakespeare");
console.log (macbeth + " " + richard);

let name = "Thor";
if (name == "Thor") {
  console.log("The Strongest Avenger");
}
else if (name == "Iron Man") {
  console.log ("The snarkest Avenger");
}

document.write("this is html");
*/

var heroes =["Thor", "Hulk", "Iron Man", "Spiderman"];

//four loop
for (var a = 0; a < heroes.length; a++) {
  console.log ("The hero is " + heroes[a]);
}

console.log (" ");

//while loop
let b = 0;
while (b < heroes.length) {
  console.log("The hero is " + heroes[b]);
  b++;
}
//leave a line
console.log (" ");
console.log (" ");

//reverse the order
let i = heroes.length - 1;
while (i >= 0) {
  console.log ("The hero is " + heroes[i]);
  i--;
  //caps HULK
  if (heroes[i] == "Hulk") {
    console.log ("The hero is " + heroes[i].toUpperCase());
  }
}

console.log (" ");

for (let k = heroes.length - 1; k >= 0; k--) {
  console.log("the hero is " + heroes[k]);
}

console.log (" ");

let team = {"green": "Hulk", "fat": "Thor", "rusty": "Iron man", "wobby": "Spiderman"}
console.log(team["green"]);


function makeName(first, last) {
  //return the first and last name combined
  return first + ' ' + last;
}

list = [];
//1,2,3 to 3,2,1
function reverseList(list) {
  let result = [];
  for (let j = list.length; j <= 0; j--) {
    result[j] = list[Math.abs(j-list.length)];
  }
  return result;
}

function findMaxSoFar(list) {
  for (let i = 0; i < list.length) {
    if (maxSoFar < list[i]) {
      maxSoFar = list[i];
    }
  }
  return maxSoFar;
}
