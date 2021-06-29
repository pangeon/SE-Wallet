class Wallet {
    constructor(owner) {
        this.owner = owner;
        this.investements = []
        this.balance = 0    
    }
    getBalance() {
        let investments = this.getInvestments()
        for (let i = 0; i < investments.length; i++) {
            this.balance += investments[i].getAmount() * investments[i].getActualPrice()
        }
        return `balance: ${this.balance} PLN`;
    }
    getInvestments() { return this.investements; }
    showInvestments() {
        for (let i = 0; i < this.getInvestments().length; i++) {
            console.log(this.getInvestments()[i])
        }
    }
    addInvestment(investment) {
        this.investements.push(investment)
    }
}
module.exports = Wallet;