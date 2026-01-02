const prompt = require("prompt-sync")();

while (true) {
    try {
        let email = prompt("Enter your email: ");
        let regex = /^[a-zA-Z0-9._%+-]+@karazon\.in$/;

        if (!regex.test(email)) {
            throw new Error("Invalid email format");
        }

        console.log(`Thank you! Confirmation sent to ${email}`);
        break;

    } catch (err) {
        console.log("Error:", err.message);
    }
}
