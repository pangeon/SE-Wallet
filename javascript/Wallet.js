const roundOff = require("./utils")

class Wallet {
    constructor(owner) {
        this.owner = owner;
        this.investements = []
        this.balance = 0
        this.amountInvested = 0    
    }
    getBalance() {
        let investments = this.getInvestments();
        for (let i = 0; i < investments.length; i++) {
            this.balance += investments[i].getAmount() * investments[i].getActualPrice()
        }
        return `balance: ${roundOff(this.balance, 3)} PLN`;
    }
    getAmountInvested() {
        let investments = this.getInvestments();
        for (let i = 0; i < investments.length; i++) {
            this.amountInvested += investments[i].getAmount() * investments[i].getBuyPrice()
        }
        return `sum of money invested: ${roundOff(this.amountInvested, 3)} PLN`;
    }
    getInvestments() { return this.investements; }
    showInvestments() {
        for (let i = 0; i < this.getInvestments().length; i++) {
            console.log(this.getInvestments()[i])
        }
    }
    getMoneyTurnover() {
        return `money turnover: ${roundOff(this.balance - this.amountInvested, 3)} PLN`
    }
    addInvestment(investment) {
        this.investements.push(investment)
    }
}
module.exports = Wallet;