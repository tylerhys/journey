import express, { json } from "express";
const app = express();
import cors from "cors";
const port = 3042;


import { toHex } from "ethereum-cryptography/utils";
import { keccak256 } from "ethereum-cryptography/keccak";
import { Signature } from "@noble/secp256k1";

app.use(cors());
app.use(json());

const balances = {
  "0xa0d7f4e6b420f475dbc4dd216877e6b6b6e2c32c": 100,
  "0x62f9454d2c107065b6c5df3b4f30c855b74fd2d3": 50,
  "0x8f18cedbdaf9e72cfc5480f7c89a5b1d06854fac": 75,
};

app.get("/balance/:address", (req, res) => {
  const { address } = req.params;
  const balance = balances[address] || 0;
  res.send({ balance });
});

app.post("/send", (req, res) => {
  const { sender, recipient, amount, signatureData, msg} = req.body;
  try{
    // Recover Signature
    const rBigInt = BigInt(signatureData.r);
    const sBigInt = BigInt(signatureData.s);
    const recovery = signatureData.recovery;
    const signature = new Signature(
      rBigInt,
      sBigInt,
      recovery
    );
    
    // Recover message hash
    const msgHash = Object.values(msg);

    // Retrieve wallet address from message hash
    const publicKey = signature.recoverPublicKey(msgHash).toRawBytes();
    const walletAddress = "0x"+toHex(keccak256(publicKey.slice(1)).slice(-20));


    if (sender!==walletAddress && isValid !== true) {
      return res.status(400).send({ message: "Signature verification failed." });
    }
    
    setInitialBalance(sender);
    setInitialBalance(recipient);

    if (balances[sender] < amount) {
      console.log('Sending insufficient balance error...');
      res.status(400).send({ message: "Insufficient balance..." });
    } else {
      balances[sender] -= amount;
      balances[recipient] += amount;
      res.send({ balance: balances[sender] });
    } 
  } catch(error){
    console.log(error);
    res.status(400).send({ message: "Error processing transaction..."})
  }
});

app.listen(port, () => {
  console.log(`Listening on port ${port}!`);
});

function setInitialBalance(address) {
  if (!balances[address]) {
    balances[address] = 0;
  }
}
