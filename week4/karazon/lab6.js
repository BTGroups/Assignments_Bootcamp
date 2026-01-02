// LAB 6: Email Simulation and Local Save

const prompt = require("prompt-sync")();

// Email input
let email = prompt("Enter your email (@karazon.in): ");
let emailRegex = /^[a-zA-Z0-9._%+-]+@karazon\.in$/;

if (!emailRegex.test(email)) {
    console.log("Invalid email format");
} else {
    // Sample invoice data
    let invoiceData = {
        invoiceNumber: "INV-12345",
        amount: 3880.4,
        date: new Date().toLocaleString()
    };

    console.log(`Invoice sent to ${email}`);
    console.log("\nInvoice JSON Data:");
    console.log(JSON.stringify(invoiceData, null, 2));

    console.log("\nThank you for shopping with us!");
}
