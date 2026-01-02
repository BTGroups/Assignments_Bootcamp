let cart = [
    { itemCode: "I101", description: "Shoes", quantity: 2, price: 1500, total: 3000 },
    { itemCode: "I102", description: "Socks", quantity: 3, price: 200, total: 600 }
];


let invoiceNumber = "INV-" + Math.floor(Math.random() * 100000);
let invoiceDate = new Date();

console.log("Invoice No:", invoiceNumber);
console.log("Date:", invoiceDate.toLocaleString());
console.log("\nItems:")
cart.forEach(item => {
    console.log(
        `${item.itemCode} | ${item.description} | Qty: ${item.quantity} | Price: ${item.price} | Total: ${item.total}`
    );
});
console.log("Invoice Generated Successfully");
