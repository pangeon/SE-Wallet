class Investment {
    constructor(name, amount, buyPrice, actualPrice, currency, currencyPrice) {
        this.name = name;
        if (amount <= 0 || actualPrice <= 0) {
            throw new Error("Negative value of amount investments or price.")
        } else {
            switch(currency) {                    
                case "USD":
                    this.buyPrice = Math.round((buyPrice * currencyPrice)*100) / 100;
                    this.actualPrice = Math.round((actualPrice * currencyPrice)*100) / 100;
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
}
module.exports = Investment;