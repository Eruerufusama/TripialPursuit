// Get reference to questions and buttons.
let questions = document.querySelector('.questions').children
let numbers = document.querySelector('.question-numbers').children

for (let i = 0; i < numbers.length; i++) {

    // Hide questions that aren't active.
    if (!numbers[i].classList.contains('active')) {
        questions[i].style.display ='none';
    }

}

function switchQuestion(index) {

    // Hide all questions and disable all buttons.
    for (let i = 0; i < numbers.length; i++) {
        questions[i].style.display = 'none';
        numbers[i].classList.remove('active');
    }

    // Show relevant question and activate relevant button.
    questions[index].style.display = 'flex';
    numbers[index].classList.add('active');
}