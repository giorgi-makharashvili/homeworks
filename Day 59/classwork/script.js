// 1)
let num1 = Number(prompt("enter number"));
let num2 = Number(prompt("enter number2"));

console.log(num1+num2);

//2)

let name1 = prompt("enter your name");

console.log("Hello, " + name1);

//3)
let form = document.getElementById("form1");
function logData(e){
    e.preventDefault();
    console.log(e.target.n1.value);
}

form.addEventListener("submit", logData);







