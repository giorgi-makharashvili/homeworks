// 1)
const p1 = document.getElementsByClassName("p1");

// 2)
const p2 = document.querySelector("#p2");
const p3 = document.querySelector(".p3");

// 3)
const img1 = document.getElementById("img1");
img1.width='100px'
img1.src="17.png"

// 4)
const p4 = document.getElementById("p4");
p4.style.color="red";
p4.style.backgroundColor="black";
p4.style.fontSize="30px";

// 5)
let x = document.createElement("p");
let x2 = document.createTextNode("hello world");

let div = document.getElementById("g1");
x.appendChild(x2);
div.appendChild(x);