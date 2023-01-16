const allEven = []
const allOdd = []

for (let x=0; x<=9; x++) {
    if (x === 0) {
            // console.log(x +  " is even");
            allEven.push(x);
    }
    else if (x % 2 === 0) {
            // console.log(x + " is even"); 
            allEven.push(x); 
    }
    else {
            // console.log(x + " is odd");
            allOdd.push(x);
    }
}
console.log(allEven);
console.log(allOdd);