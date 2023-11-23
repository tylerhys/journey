async function run() {
    const { create } = await import('ipfs-http-client');
    const ipfs = await create();
    
    // we added three attributes, add as many as you want!
    const metadata = {
        path: '/',
        content: JSON.stringify({
            name: "Mama",
            attributes: [
            {
                "trait_type": "Cute",
                "value": "29" 
            },
            {
                "trait_type": "Love",
                "value": "05"
            },
            {
                "trait_type": "Web3",
                "value": "13"
            }
            ],
            // update the IPFS CID to be your image CID
            image: "https://ipfs.io/ipfs/QmNUNw8T9sMmw7rfNobCtW1oiHa5kNt8v5KRzaEsBAYArY",
            description: "Its the Mama!"
        })
    };

    const result = await ipfs.add(metadata);
    console.log(result);

    process.exit(0);
}

run();