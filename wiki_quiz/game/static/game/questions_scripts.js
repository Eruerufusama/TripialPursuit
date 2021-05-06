// Get reference to questions and buttons.
let questions = document.querySelector('.questions').children;
let numbers = document.querySelector('.question-numbers').children;
let answerTexts = document.querySelectorAll('.answer-text');

for (let i = 0; i < numbers.length; i++) {
    answerTexts[i].style.display ='none';

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

    let answerText = activeQuestion.querySelector('.answer-text');

    // Show correct and incorrect answers when an answer is clicked.
    if (answers[index].classList.contains('correct')) {
        answers[index].style.backgroundColor = "#45f556";

        answerText.innerHTML = "That is correct!";
        answerText.style.display ='flex';
    }
    else {
        answers[index].style.backgroundColor = "#f54b45";

        for (i = 0; i < answers.length; i++) {
            if (answers[i].classList.contains('correct')) {
                answers[i].style.backgroundColor = "#45f556";

                answerText.innerHTML = "incorrect!";
                answerText.style.display ='flex';
            }
        }
    }

    // Disable all buttons.
    for (const button of answers) {
        button.disabled = true;
    }

}