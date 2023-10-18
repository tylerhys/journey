//runCallback.js
function runCallback(callbackFunction) {
    setTimeout(() => {
        callbackFunction();
    }, 1000);
}

// dialogCallback.js
class Dialog {
    constructor() {
        this.callbackFunctions = [];
    }
    close() {
        this.callbackFunctions.forEach((callbackFn) => {
            callbackFn();
        });
    }
    onClose(callbackFunction) {
        this.callbackFunctions.push(callbackFunction);
    }
}

// forEach.js
function forEach(arr, callback) {
    for (let i = 0; i < arr.length; i++) {
        callback(arr[i], i);
    }
}

// map.js
function map(arr, callback) {
    const newArr = [];
    for (let i = 0; i < arr.length; i++) {
        newArr[i] = callback(arr[i], i);
    }
    return newArr;
}