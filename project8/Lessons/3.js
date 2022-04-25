// while(true) {
//     rdNum = Math.random();
//     const ask = prompt('Enter a Number: ');
//     if ( ask == rdNum){
//         alert('Waoooh, You guessed right');
//     } else {
//         alert('Sorry Incorrect no , Try Harder...')
//     }
// }

while (true) {
    let num = prompt('Guess a number: ');
        num = Number(num);
    const randNumber = Math.ceil(Math.random() * 10);
    if (num == randNumber){
        alert('You WIN !!!!');
        break;
    } else {
        console.log("You guessed", num, "But the right number was: ", randNumber);
    }
}