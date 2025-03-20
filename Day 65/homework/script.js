// 4)
function Me(name,age,hairColor,lastName,height) {
    this.name = name;
    this.age = age;
    this.hairColor = hairColor;
    this.lastName = lastName;
    this.height = height;
}

const Me2 = new Me ("gio", 16, "brown", "maxarashvili", 178)

//5)
function Bike(color,maxSpeed,brand,Method) {
    this.color = color;
    this.maxSpeed = maxSpeed;
    this.brand = brand;
    this.increasespeed = Method;
}

function increasespeed() {
    maxSpeed += 200
}
const Bike2 = new Bike("black", 300, "ninja" );