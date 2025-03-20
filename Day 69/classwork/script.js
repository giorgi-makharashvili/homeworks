// 1)
const date = new Date()

// 2)
console.log(date)

console.log(date.getFullYear())
console.log(date.getMonth())
console.log(date.getDate())
console.log(date.getDay())
console.log(date.getHours())
console.log(date.getMinutes())
console.log(date.getSeconds())
console.log(date.getMilliseconds())

// 3)
const myp = document.getElementById("myp");

setInterval(() => {
    const date = new Date();

    myp.textContent =  `${date.getHours()}:${date.getMinutes()}:${date.getSeconds()}`
} ,1000)