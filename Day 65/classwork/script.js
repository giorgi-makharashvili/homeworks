//1)
// მსგავსება: jsში ვქმნით  ობჯექთის სახელს, ვწერთ key, მასში შედის keyს მნიშვნელობა ისევე როგორც პითონში.
// განსხვავება: ობჯექთის შექმნის შემდეგ key ბრჭყალებში არისმება. პითონში ეს აუცილებელია

//2)
const Obj1 = {
    name: "gio",
    lastname: "maxara",
    sayhello: function() {console.log("hello I am gio")}
}

//3)
// ფუნქცია შეგვიძლია გამოვიყენოთ რამდენიმე data typeზე.
// გამოყენება ხდება მხოლოდ ერთ data typeზე.

//4)
function Person(name,lastname,age) {
    this.name = name;
    this.lastname = lastname;
    this.age = age
}

const Person1 = new Person("gio","maxara", 16);

//5)

function Car(brand, model, year, color, horsePower, Method) {
    this.brand = brand;
    this.model = model;
    this.year = year;
    this.color = color;
    this.horsePower = horsePower;
    this.increasedpower = Method;
}
function increasedpower() {
    horsePower +=100
}

const Car1 = new Car("porsche","911 gt3 rs","2024","gray","518")