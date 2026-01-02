const prompt = require("prompt-sync")();
let grandTotal = 0
let itemCart = []

const Item = {
    itemCode : null,
    description : "",
    quantity : 0,
    price : 0
}


while (true){
 try {    const item = Object.create(Item)
    item.itemCode = prompt("enter the item code: ")
    item.description = prompt("enter the name: ")
    item.quantity = Number(prompt(`Enter the quantity of ${item.description}: `))
    item.price = Number(prompt(`Enter the price for the ${item.description}: `))
    
    itemCart.push(item)
    grandTotal = grandTotal +  item.price * item.quantity

    //membership chekcing
    member = prompt("Are you a member?")

    answer = prompt("would you like to add an another item? (Y/N)")
    if (answer == "N" || answer == "n") {
        break
    } }
    catch(err) {
        console.log(err.message);
    }
}

//lab1 
console.log(`Items in cart : ${itemCart}`)
console.log(`Grand Total for items : ${grandTotal}`)


