function getDiscountFunction(type) {
    let rate = 0;

    if (type === "SILVER") rate = 0.05;
    if (type === "GOLD") rate = 0.10;
    if (type === "PLATINUM") rate = 0.15;

    return function (amount) {
        return amount * rate;
    };
}

let subtotal = 2000;
let discountFn = getDiscountFunction("GOLD");
let discount = discountFn(subtotal);

console.log("Subtotal:", subtotal);
console.log("Discount:", discount);
