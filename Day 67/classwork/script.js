//1)
let arr1 = new Array(1,2,3,4,5);
console.log(arr1[0]);
console.log(arr1[1]);
console.log(arr1[2]);
console.log(arr1[3]);
console.log(arr1[4]);

//2)
let arr2 = new Array(4);
// აქ შეიქმნა 4 ცარიელი ცვლადი, ეს რიცხვი მიგვითითებს მათ რაოდენობას ანუ lenს.

//3)
let arr3 = [1,2,3];

//4)
let x = [];
x["name"] = "gio";
x["surname"] = "maxarashvili";
x["age"] = 16;
console.log(x)
// რადგან აქ უბრალოდ ობიექტი შეიქმნა array ში და ის არ ითვლება მის ნაწილად, ამიტომ ზომა 0ს აჩვენებს.