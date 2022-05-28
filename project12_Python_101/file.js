var x=0;
var y="";
var z=4;
if(x==y){
  z++;
}

// console.log("type of y", typeof(y) )
// console.log(z);

// console.log( !(false || true) )

// const button = document.querySelector('button');

// button.addEventListener('click', event => {
//    waitfunction();
// });
// async function waitfunction() {
// setTimeout('alertbox()', 1000);
// }
// function alertbox() {
//     window.alert('10');   
// }

// const name = {
//     "data" : "item1",
//     "data2" : "item2" 
// }

// function makeAPromise(resolve, reject) {
//     resolve(1);
//     setTimeout(resolve, 2000, 2);
//     }
//     let promise = new Promise(makeAPromise);
//     promise.then(alert);

function display(word) {
    document.getElementById("demo").innerHTML = word;
  }
  
  function wordOne() { display("Go"); }
  function wordTwo() { display("Stop"); }
  function wordThree() { display("Yield"); }
  
  wordThree();
  wordTwo();
  wordOne(); 
  