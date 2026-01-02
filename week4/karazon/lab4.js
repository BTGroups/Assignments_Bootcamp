const prompt = require("prompt-sync")();

let totalWithTax = Number(prompt("Enter total with tax: "));
let paymentMode = prompt("Payment mode (Card/UPI/Cash): ").toUpperCase();

let surcharge = 0;
let convenienceFee = 0;

if (paymentMode === "CARD" && totalWithTax < 1000) {
    surcharge = totalWithTax * 0.025;
} else {
    convenienceFee = totalWithTax * 0.01;
}

let finalTotal = totalWithTax + surcharge + convenienceFee;

console.log("Final Total:", finalTotal);
