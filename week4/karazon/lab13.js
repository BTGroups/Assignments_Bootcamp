// LAB 13: Callback for Post-Billing Workflow

function completeBilling(callbackFn) {
    console.log("Final bill calculated");
    callbackFn();
}

// Callback function
function postBillingAction() {
    console.log("Invoice displayed");
    console.log("Thank you for shopping!");
}

// Execute
completeBilling(postBillingAction);
