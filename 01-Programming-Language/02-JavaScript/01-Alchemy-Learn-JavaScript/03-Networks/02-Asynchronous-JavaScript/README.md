## **Topic Summary: Callback Function**
Callback Function
```
function simpleFunction(fn) {
    // invoke the callback function
    fn();
}

simpleFunction(function callbackFunction() {
    console.log('hi');
});
```
setTimeout
```
setTimeout(function callback() {
    // the code to run after 1000 milliseconds
}, 1000);
```

## **Topic Summary: Intro to Promises**
Promise
```
const promise = getServerData();

// similar to using a callback function argument,
// except we wire up the callback using .then 
promise.then(function(data) {
    // this function is called asynchronously
    // once the server has responded with data
    console.log('got data', data);
});
```
Async/Await
```
async function getData() {
    const result = await serverCall();

    // this will not run until serverCall resolves/rejects
    return result;
}
```
## **Topic Summary: Promise Library**
```
Need to learn more...
ATM example, view Pact.js
```

## **More Info**
**Set Timeout Documentation:** [Link](https://developer.mozilla.org/en-US/docs/Web/API/setTimeout)
**Promise Documentation:** [Link](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
**async Documentation:** [Link](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)
**Promise Chain Documentation:** [Link](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/then#chaining)