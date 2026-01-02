// LAB 12: Inventory System with Promises

function checkInventory(itemCode, requestedQty) {
    return new Promise((resolve, reject) => {
        // Mock inventory stock
        let stockQuantity = 50;

        console.log(`Checking stock for Item ${itemCode}...`);

        if (requestedQty <= stockQuantity) {
            resolve(`Stock available for item ${itemCode}`);
        } else {
            reject(`Insufficient stock for item ${itemCode}`);
        }
    });
}

// Test the promise
checkInventory("I101", 20)
    .then(result => {
        console.log(result);
        console.log("Proceed to billing");
    })
    .catch(error => {
        console.log(error);
        console.log("Cannot proceed to billing");
    });
