function roundOff(value, precision) {
    let toRound = value * 10 ** precision
    return Math.round(toRound) / 10 ** precision;
}
module.exports = roundOff