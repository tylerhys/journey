// retrieve a prop that is deeply nested within objects
// i.e. { prop: { prop: { prop: 3 }}} => 3

// My answer
function deepRetrieval(obj) {
    if (typeof obj.prop === "object"){
        return deepRetrieval(obj.prop);
    }
    else {
        return obj.prop;
    }
}

// Default Answer
function deepRetrieval(obj) {
    while(obj.prop) {
        obj = obj.prop;
    }
    return obj;
}