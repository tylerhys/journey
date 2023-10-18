## **Hash**
SHA256 Function
```
const { sha256 } = require("ethereum-cryptography/sha256");
const { toHex, utf8ToBytes } = require("ethereum-cryptography/utils");

const aBytes = utf8ToBytes("string");   // String to Bytes
const aHash = sha256(aBytes);           // Bytes to Hash
const aHex = toHex(aHash);              // Hash to Hexadecimal for comparison
```

## **Public Key Cryptography**
Hashing Messages
```
const bytes = utf8ToBytes("Message"); // String to Bytes
const hash = keccak256(bytes); // Bytes to Hash
console.log(toHex(hash)); // Hash to Hexadecimal
```
Sign Message
```
secp.sign(messageHash, PRIVATE_KEY, { recovered: true });
```
Recover Public Key
```
secp.recoverPublicKey(hashMessage(message),signature,recoveryBit);
```

## **More Info**
**Uint8Array Documentation:** [Link](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array)
**UTF-8:** [Link](https://en.wikipedia.org/wiki/UTF-8)
**RSA Crypto System**[Link](https://en.wikipedia.org/wiki/RSA_(cryptosystem))
**ECDSA Crypto System**[Link](https://en.wikipedia.org/wiki/Elliptic_Curve_Digital_Signature_Algorithm)
**Cryptography Library**[Link](https://github.com/paulmillr/noble-secp256k1/tree/1.7.1)
**Pub Key Recovery from Sig**[Link](https://cryptobook.nakov.com/digital-signatures/ecdsa-sign-verify-messages#ecdsa-public-key-recovery-from-signature)
**Sign Msg**[Link](https://github.com/paulmillr/noble-secp256k1/tree/1.7.1#signmsghash-privatekey)
**BTC Wallet Addy**[Link](https://en.bitcoin.it/wiki/Technical_background_of_version_1_Bitcoin_addresses)