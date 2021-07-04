// Sample Wallet

const Wallet = require("./Wallet")
const Investment = require("./Investment")

function init(
            priceUSD, 
            priceKGHM, 
            priceALCOA, 
            priceGENERALI, 
            priceINVESTOR,
            priceINVESTOR_BALANCED,
            pricePKO_BUILD_INFRASTRUCTURE,
            priceUNIQA_GLOBAL_MA,
            pricePKO_TECH_AND_GI,
            pricePKO_AMERICAN_ME,
            priceTOP_25
        ) 
{
    let wallet_cecherz = new Wallet("Kamil Cecherz")

    let KGHM = new Investment("KGHM", 10, 203.69, 
    priceKGHM, "PLN")

    let ALCOA = new Investment("ALCOA INC", 15, 41.54, 
    priceALCOA, "USD", priceUSD)

    let GENERALI = new Investment("GENERALI", 38.774719, 128.95, 
    priceGENERALI, "PLN")

    let INVESTOR_NEW_TECHNOLOGY = new Investment("INVESTOR_NOWYCH_TECHNOLOGII", 14.355441, 208.98, 
    priceINVESTOR, "PLN")

    let INVESTOR_BALANCED = new Investment("INVESTOR_ZRÓWNOWAŻONY", 2.876506, 869.11, 
    priceINVESTOR_BALANCED, "PLN")

    let PKO_BUILD_INFRASTRUCTURE = new Investment("PKO_INFRASTRUKTURY_BUDOW.GLOBALNY", 2.876506, 20.576, 
    pricePKO_BUILD_INFRASTRUCTURE, "PLN")

    let UNIQA_GLOBAL_MACRO_ALLOCATION = new Investment("UNIQA_GLOBALNEJ_MAKROALOKACJI", 19.67729, 127.05, 
    priceUNIQA_GLOBAL_MA, "PLN")

    let PKO_TECH_AND_GLOBAL_INNOVATION = new Investment("PKO_TECH_I_INNOWACJI_GLOBALNY", 0.255, 391.54, 
    pricePKO_TECH_AND_GI, "PLN")

    let PKO_AMERICAN_MARKET_EQUITY = new Investment("PKO_AKCJI_RYNKU_AMERYKAŃSKIEGO", 0.611, 163.68, 
    pricePKO_AMERICAN_ME, "PLN")

    let INVESTOR_TOP_25 = new Investment("INVESTOR_TOP_25", 0.257639, 388.14, 
    priceTOP_25, "PLN")

    const investments = [
        KGHM, 
        ALCOA, 
        GENERALI, 
        INVESTOR_NEW_TECHNOLOGY, 
        INVESTOR_BALANCED, 
        PKO_BUILD_INFRASTRUCTURE, 
        UNIQA_GLOBAL_MACRO_ALLOCATION, 
        PKO_TECH_AND_GLOBAL_INNOVATION,
        PKO_AMERICAN_MARKET_EQUITY,
        INVESTOR_TOP_25
    ]
    for (let i = 0; i < investments.length; i++) {
        wallet_cecherz.addInvestment(investments[i])
    }
    console.log(wallet_cecherz.showInvestments())
    console.log(wallet_cecherz.getBalance())
    console.log(wallet_cecherz.getAmountInvested())
    console.log(wallet_cecherz.getMoneyTurnover())
}
init(3.79,  // priceUSD 
    187.65, // priceKGHM
    37.53,  // priceALCOA 
    129.29, // priceGENERALI
    232.60, // priceINVESTOR
    855.75, // priceINVESTOR_BALANCED
    115.28, // pricePKO_BUILD_INFRASTRUCTURE
    114.78, // priceUNIQA_GLOBAL_MA
    399.84, // pricePKO_TECH_AND_GI
    166.15, // pricePKO_AMERICAN_ME
    391.98  // priceTOP_25    
)
