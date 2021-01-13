const togglePassword = document.querySelector('#togglePassword');
const toggleConfirm = document.querySelector('#toggleConfirm');
const password = document.querySelector('#password');
const confirm = document.querySelector('#confirm');

togglePassword.addEventListener('click', function (e) {
    // toggle the type attribute
    const type = password.getAttribute('type') === 'password' ? 'text' : 'password';
    password.setAttribute('type', type);
    // toggle the eye slash icon
    this.classList.toggle('fa-eye-slash');
});

toggleConfirm.addEventListener('click', function (e) {
    // toggle the type attribute
    const type = confirm.getAttribute('type') === 'password' ? 'text' : 'password';
    confirm.setAttribute('type', type);
    // toggle the eye slash icon
    this.classList.toggle('fa-eye-slash');
});