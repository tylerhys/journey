function setMessage(contract, signer) {
    return contract.connect(signer).modify("hello");
}

module.exports = setMessage;