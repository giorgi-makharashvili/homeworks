
// 1)
function sum1(arr) {
    let x = 0;
    for (let i = 0; i < arr.length; i++){
        x += arr[i]
    }
    return x;
}

console.log(sum1([1,2,3]))


// 2)
function minMax(arr) {
    return Math.min(arr), Math.max(arr);
}

console.log(minMax([1,2,3]))
// 3)
function Create(num1,num2) {
    const arr = [];
    for (let i = num1; i < num2; i++) {
        arr.push(i);
    }
    
    return arr;
}

console.log(Create(1,10))

// 4)
function x(arr) {
    const y = []
    for (let i = 0; i < arr.length; i++) {
        y.push(i**2);
    }
    return y;
}
console.log(x([1,2,3,4,5]))

// 5)
function rounder(num) {
    return [Math.floor(num), Math.ceil(num), Math.round(num)];
}
console.log(rounder(3.24))