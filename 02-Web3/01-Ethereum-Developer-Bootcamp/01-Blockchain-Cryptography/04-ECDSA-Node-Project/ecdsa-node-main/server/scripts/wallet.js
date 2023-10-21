import { secp256k1 } from 'ethereum-cryptography/secp256k1';
import { toHex, utf8ToBytes } from "ethereum-cryptography/utils";
import { keccak256 } from "ethereum-cryptography/keccak"
// import * as secp from '@noble/secp256k1';

// Store Private Key
const privateKey="a832d3d10a0b6b2685c47d59ec56a2251f719e78d4db1d87735d9d1e46b8527e";
const recipient = "0x62f9454d2c107065b6c5df3b4f30c855b74fd2d3";
const amount = 5;

// Get Public Key and Wallet Address
const publicKey = secp256k1.getPublicKey(privateKey);
console.log('public key:', toHex(publicKey));

const walletAddress = "0x"+toHex(keccak256(publicKey.slice(1)).slice(-20));
console.log('wallet address:', walletAddress);

// Generate Signature
const msg = "Transfer "+ amount + "ETH to " + recipient;
console.log(msg);

const msgHash = keccak256(utf8ToBytes(msg));
console.log('message hash:', toHex(msgHash)); // Hash to Hexadecimal

const signature = secp256k1.sign(msgHash,privateKey);
console.log(signature); // Hash to Hexadecimal

// Verify Signature
const pb = signature.recoverPublicKey(msgHash);
console.log('recover:',pb);
const hexPb = pb.toHex();
if (hexPb === toHex(publicKey)){
    console.log("They are the same");
}
console.log(hexPb);
const isValid = secp256k1.verify(signature,msgHash,hexPb);
console.log('signature is valid:',isValid);
