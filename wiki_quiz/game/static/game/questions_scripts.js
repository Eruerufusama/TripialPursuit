// Get reference to questions and buttons.
let questions = document.querySelector('.questions').children
let numbers = document.querySelector('.question-numbers').children

for (let i = 0; i < numbers.length; i++) {

    // Hide questions that aren't active.
    if (!numbers[i].classList.contains('active')) {
        questions[i].style.display ='none';
        questions[i].classList.remove('active-question');
    }

}

function switchQuestion(index) {

    // Hide all questions and disable all buttons.
    for (let i = 0; i < numbers.length; i++) {
        questions[i].style.display = 'none';
        questions[i].classList.remove('active-question');

        numbers[i].classList.remove('active');
    }

    // Show relevant question and activate relevant button.
    questions[index].style.display = 'flex';
    questions[index].classList.add('active-question');

    numbers[index].classList.add('active');
}

function showAnswer(index) {
    let activeQuestion = document.querySelector('.active-question');
    let answers = activeQuestion.querySelector('.answers').children;

    if (answers[index].classList.contains('correct')) {
        console.log('correct!');
        answers[index].style.backgroundColor = "#45f556";
    }
    else {
        console.log('That is false!');
        answers[index].style.backgroundColor = "#f54b45";

        for (const button of answers) {
            if (button.classList.contains('correct')) {
                button.style.backgroundColor = "#45f556";
            }
        }
    }

    for (const button of answers) {
        button.disabled = true;
    }
}