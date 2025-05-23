console.log("Hello from JavaScript!");
document.addEventListener('DOMContentLoaded', function() {
    const learnerBtn = document.getElementById('learner-btn');
    const teacherBtn = document.getElementById('teacher-btn');
    const parentBtn = document.getElementById('parent-btn');
    const learnerSignup = document.getElementById('learner-signup');

    learnerBtn.addEventListener('click', function() {
        setActiveButton(learnerBtn);
        showSignupBox(learnerSignup);
    });

    teacherBtn.addEventListener('click', function() {
        setActiveButton(teacherBtn);
        hideSignupBox(learnerSignup);
    });

    parentBtn.addEventListener('click', function() {
        setActiveButton(parentBtn);
        hideSignupBox(learnerSignup);
    });

    function setActiveButton(button) {
        document.querySelectorAll('.role-button').forEach(btn => btn.classList.remove('active'));
        button.classList.add('active');
    }

    function showSignupBox(box) {
        box.style.display = 'block';
        box.style.animation = 'fadeIn 0.5s ease-in-out';
    }

    function hideSignupBox(box) {
        box.style.display = 'none';
    }
});
