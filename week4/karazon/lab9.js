const prompt = require("prompt-sync")();
class ValidationError extends Error {
    constructor(message) {
        super(message);
        this.name = "ValidationError";
    }
}

try {
    let quantity = Number(prompt("Enter quantity: "));
    let price = Number(prompt("Enter price: "));

    if (quantity <= 0) {
        throw new ValidationError("Quantity must be greater than 0");
    }

    if (price <= 0) {
        throw new ValidationError("Price must be greater than 0");
    }

    console.log("Valid input. Total:", quantity * price);

} catch (err) {
    console.log(err.name + ":", err.message);
} finally {
    console.log("Input validation completed");
}