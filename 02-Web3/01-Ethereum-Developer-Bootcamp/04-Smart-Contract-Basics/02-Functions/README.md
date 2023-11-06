## Functions
Functions
```
function <function name> <function type> <return types>{
    return < ... >;
}

function getName() public view returns (string _name){
    return name;
}

// Declarations
view: this function promises that** NO state will be changed, only read**
pure: this function promises that NO state will be changed nor read

// Visibility
public - any contract or EOA can call into this function
external - only other contracts (external to the current contract) and EOAs can call, no internal calling
internal - only this contract along with its inheritance chain can call
private - only this contract can call

```
