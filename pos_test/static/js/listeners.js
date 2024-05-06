function handleChange(event) {
    const checkbox = event.target;
    const form = checkbox.closest('.quiz-form');
    const formData = new FormData(form);
    const formId = form.id;

    formData.append('id', formId);
    formData.append('type', 'quiz');

    fetch('/questionnaire/', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        const visibleList = data.visible;
        const hiddenList = data.hidden;

        visibleList.forEach(name => {
            const element = document.getElementById(name);
            if (element) {
                element.style.display = 'block';
            }
        });

        hiddenList.forEach(name => {
            const element = document.getElementById(name);
            if (element) {
                element.style.display = 'none';
            }
        });
    });
}


function handleQuestionChange(event) {
    const input = event.target;
    const form = input.closest('.question-form');
    const formData = new FormData(form);
    const formId = form.id;

    formData.append('id', formId);
    formData.append('type', 'question');

    const answers = formData.getAll('answer');

    if (!answers.includes('')) {
    fetch('/questionnaire/', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        const visibleList = data.visible;
        const hiddenList = data.hidden;

        visibleList.forEach(name => {
            const element = document.getElementById(name);
            if (element) {
                element.style.display = 'block';
            }
        });

        hiddenList.forEach(name => {
            const element = document.getElementById(name);
            if (element) {
                element.style.display = 'none';
            }
        });
    });
}
}


function addListeners() {
    const forms = document.querySelectorAll('.quiz-form');

    forms.forEach(form => {
        const checkboxes = form.querySelectorAll('input[type="checkbox"], input[type="radio"]');
        
        checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', handleChange);
        });
    });
}


function addQuestionsListeners() {
    const forms = document.querySelectorAll('.question-form');

    forms.forEach(form => {
        const textInputs = form.querySelectorAll('input[type="text"]');
        
        textInputs.forEach(text => {
        text.addEventListener('blur', handleQuestionChange);
        });
    });
}



document.addEventListener('keydown', function(event) {
    if (event.key === "Enter") {
        event.preventDefault();
    }
});


document.addEventListener('DOMContentLoaded', () => {
    addListeners();
    addQuestionsListeners();
});

