class LinkedList {
    constructor() {
        this.head = null;
    }

    addFirst(node) {
        node.next = this.head;
        this.head = node; 
    }

    addLast(node) {
        if(!this.head) {
            this.head = node;
            return;
        }
        
        let ptr = this.head;
        while(ptr.next) ptr = ptr.next;
        ptr.next = node;
    }

    indexOf(node) {
        let idx = 0;
        let ptr = this.head;

        do {
            if(ptr === node) {
                return idx;
            }
            ptr = ptr.next;
            idx++;
        }
        while(ptr)
    }

    removeAt(index) {
        if (index === 0) {
            this.head = this.head.next;
            return;
        }

        let idx = 0;
        let node = this.head;

        while(idx < (index - 1)) {
            node = node.next;
            idx++;
        }

        node.next = node.next.next;
    }
}