const roundOff = require("./utils")

class Investment {
    constructor(name, amount, buyPrice, actualPrice, currency, currencyPrice) {
        this.name = name;
        if (amount <= 0 || actualPrice <= 0) {
            throw new Error("Negative value of amount investments or price.")
        } else {
            switch(currency) {                    
                case "USD":
                    this.buyPrice = roundOff(buyPrice * currencyPrice, 3);
                    this.actualPrice = roundOff(actualPrice * currencyPrice, 3);
                    break;
                default:
                    this.buyPrice = buyPrice;
                    this.actualPrice = actualPrice;

            }
            this.amount = amount;
            this.currency = currency;
            this.currencyPrice = currencyPrice;
        }
    }
    getName() { return this.name; }
    getAmount() { return this.amount; }
    getActualPrice() { return this.actualPrice; }
    getBuyPrice() { return this.buyPrice }
}
module.exports = Investment;