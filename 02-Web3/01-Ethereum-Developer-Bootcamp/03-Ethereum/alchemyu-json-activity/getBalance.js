require('dotenv').config();
const { API_KEY } = process.env;
const axios = require('axios');
const url = `https://eth-mainnet.g.alchemy.com/v2/${API_KEY}`;

async function getBalance(address) {
    const response = await axios.post(url, {
        jsonrpc: "2.0",
        id: 1,
        method: "eth_getBalance", // <-- fill in the method
        params: [
            address,
            "latest"
        ],  // <-- fill in the params
    });

    // use this if you want to inspect the response data!
    // console.log(response.data);

    return response.data.result// TODO: return the balance of the address
}

module.exports = getBalance;