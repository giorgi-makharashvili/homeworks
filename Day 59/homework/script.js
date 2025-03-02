

//2)
let num1 = Number(prompt("enter number1"));
let num2 = Number(prompt("enter number2"));
let num3 = Number(prompt("enter number3"));

console.log(num1+num2+num3);

//3)
const form = document.getElementById("form1");

function logData(e) {
    e.preventDefault();
    console.log(e.target.input1.value+e.target.input2.value);
}

form.addEventListener("submit", logData);

//5) იმაში რომ მარტივად მივწვდეთ formში არსებულ inputს nameის დახმარებით.