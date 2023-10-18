// Order.js
const { makeFood } = require('./Kitchen');

class Order {
    constructor() {
        this.isReady = false;
    }
    request(food) {
        makeFood(food).then(() => {
            this.isReady = true;
        }).catch((error) => {
            this.error = error;
        });
    }
}

//timer.js (create promise)
function timer() {
    return new Promise((resolve, reject) => {
        setTimeout(()=>{
            resolve();
            },1000)
    });
}

// handleResults.js (Async Await)
const { getResults } = require('./lab');
const { sendResults } = require('./messaging');
const { logResponse, logError } = require('./logs');

async function handleResults(patientId) {
    try {
    const results = await getResults(patientId);
    const response = await sendResults(patientId, results);
    await logResponse(response);
    }
    catch(ex){
        logError(ex);
    }
}