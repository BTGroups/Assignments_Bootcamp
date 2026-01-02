let discountedTotal = Number(prompt("Enter discounted total: "));

let gstRate = 0.18;
let platformFeeRate = 0.002;

let gstAmount = discountedTotal * gstRate;
let platformFee = discountedTotal * platformFeeRate;
let totalWithTax = discountedTotal + gstAmount + platformFee;

console.log("GST:", gstAmount);
console.log("Platform Fee:", platformFee);
console.log("Total with Tax:", totalWithTax);
