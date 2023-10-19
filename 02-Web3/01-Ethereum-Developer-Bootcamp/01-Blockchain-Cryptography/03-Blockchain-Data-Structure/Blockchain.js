const Block = require('./Block');

class Blockchain {
    constructor() {
        this.chain = [ new Block() ];
    }

    addBlock(block){

        block.previousHash = this.chain[this.chain.length - 1].toHash();
        this.chain.push(block);
    }

    isValid(){
        for(let i = 0; i < this.chain.length; i++){
            if(this.chain[i].toHash().toString() !== this.chain[i+1].previousHash.toString()){
                return false;
            }
            else {
                return true;
            }
        }
    }
}