async function processPayment(){
    console.log("Processing Payment....")
    return new Promise(resolve => {
        setTimeout(() => {
            resolve.apply("PAYMENT SUCCESSFUL!!")
        }, 2000);
    });
}

(async () => {
    let status = await processPayment();
    console.log(status);
})();