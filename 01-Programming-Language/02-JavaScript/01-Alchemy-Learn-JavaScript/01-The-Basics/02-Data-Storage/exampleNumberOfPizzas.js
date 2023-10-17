const ORDER_TYPES = require('./exampleOrderTypes');

function numberOfPizzas(orders) {
    let sum = 0;
    for (i = 0; i < orders.length; i++){
        if (orders[i].type === ORDER_TYPES.PIZZA)
        {
            sum = sum + orders[i].pizzas;
            }
    }
    return sum;
}