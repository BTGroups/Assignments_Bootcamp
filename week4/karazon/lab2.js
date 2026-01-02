const prompt = require("prompt-sync")

let grandTotal = Number(prompt("Enter the grand Total:"))
let discountRate = 0

let member = prompt("Member? (Y/N): ").toUpperCase();
if (member === "Y"){
    let type = prompt("Enter the membership type(Gold/silver/platinum) :").toUpperCase();
    if (type === "SILVER") discountRate = 0.05;
    if (type === "GOLD") discountRate = 0.10;
    if (type === "PLATINUM") discountRate = 0.15;
}

let discountAmount = grandTotal * discountRate;
let discountedTotal = grandTotal - discountAmount;

console.log("Discount : ", discountAmount);
console.log("discounted total : ", discountedTotal);