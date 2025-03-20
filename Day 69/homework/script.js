//2)
const myp = document.getElementById("myp");

setInterval(() => {
    const date = new Date();

    myp.textContent =  `${date.getMinutes()}:${date.getSeconds()}`
} ,1000)

//3)
let i = 0;
const x =setInterval(() => {
    console.log(i);
    i++;
    if (i >= 16) {
        clearInterval(x)
    }


} , 500)

// 4)
setTimeout(() => { console.log(1);
}, 2000)

setTimeout(() => { console.log(2);
}, 1000)

setTimeout(() => { console.log(3);
}, 3000)
