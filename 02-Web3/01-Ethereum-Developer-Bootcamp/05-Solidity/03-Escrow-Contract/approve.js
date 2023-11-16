function approve(contract, arbiterSigner) {
    contract.connect(arbiterSigner).approve();
}

module.exports = approve;