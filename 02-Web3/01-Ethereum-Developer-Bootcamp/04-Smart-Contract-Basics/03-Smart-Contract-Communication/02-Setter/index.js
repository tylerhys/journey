async function setValue(contract) {
    return contract.modify(10);
}

module.exports = setValue;