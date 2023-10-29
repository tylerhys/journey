const axios = require('axios');
const niceList = require('../utils/niceList.json');
const MerkleTree = require('../utils/MerkleTree');
const prompt = require("prompt-sync")()
const verifyProof = require('../utils/verifyProof');

const serverUrl = 'http://localhost:1225';

async function main() {
  // TODO: how do we prove to the server we're on the nice list? 
  const name = prompt("Which name do you want to check?");
  if(name == null){
    alert("You have to type a name");
  }
  const tree = new MerkleTree(niceList);

  // Find the index of the name and get proof from merkle tree.
  const index = niceList.findIndex(n => n === name);
  const proof = tree.getProof(index);

  const { data: gift } = await axios.post(`${serverUrl}/gift`, {
    // TODO: add request body parameters here!
    name,
    proof
  });

  console.log({ gift });
}

main();