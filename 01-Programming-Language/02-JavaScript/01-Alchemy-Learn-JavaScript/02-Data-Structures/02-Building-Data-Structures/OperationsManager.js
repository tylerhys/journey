const Stack = require('./Stack');

class OperationManager {
    constructor() {
        this.operations = new Stack();
        this.undos = new Stack();
    }

    addOperation(operation) {
        this.operations.push(operation);
    }

    undo() {
        const operation = this.operations.pop();
        this.undos.push(operation);
    }

    redo() {
        const operation = this.undos.pop();
        this.operations.push(operation);
    }

    redoAll() {
        while(!this.undos.isEmpty()) {
            this.redo();
        }
    }
}

const manager = new OperationsManager();