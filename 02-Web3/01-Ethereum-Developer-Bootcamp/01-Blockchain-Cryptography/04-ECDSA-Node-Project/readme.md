## ECDSA Node Project

This project simulates how a client and server facilitate transfers between different addresses on the Ethereum blockchain.
For this project, the private keys are entered into the wallet as per how a browser wallet (i.e. Metamask) holds the private keys in order to sign a transaction.

Originally, the video instructions show how passing the private keys over to sign on the server side can be done but that posses as a security risk. Hence, the encryption of the message and signing is done on the client side and is passed to the server side in order to validate and conduct the transfer. 

A dashboard of the available users are also present at the bottom where clicking on them will prompt the wallet information so that tests can be carried out.