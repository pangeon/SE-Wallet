const Wallet = require("./Wallet")
const Investment = require("./Investment")

function init(priceUSD, priceKGHM, priceALCOA) {
    let wallet_cecherz = new Wallet("Kamil Cecherz")

    let KGHM = new Investment("KGHM", 10, 203.69, priceKGHM, "PLN")
    let ALCOA = new Investment("ALCOA INC", 15, 41.54, priceALCOA, "USD", priceUSD)

    wallet_cecherz.addInvestment(KGHM)
    wallet_cecherz.addInvestment(ALCOA)

    console.log(wallet_cecherz.showInvestments())
    console.log(wallet_cecherz.getBalance())
}
init(3.80, 187.90, 36.09)
