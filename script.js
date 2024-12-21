// Dummy user data (for demo purposes)
const users = {
    "john": "12345",  // username: password
    "jane": "password123"
};

// Show the login page initially
const loginPage = document.getElementById('loginPage');
const createAccountPage = document.getElementById('createAccountPage');
const welcomePage = document.getElementById('welcomePage');
const errorMessage = document.getElementById('error-message');
const createAccountLink = document.getElementById('createAccountLink');

// Handle login submission
document.getElementById('loginForm').addEventListener('submit', function(e) {
    e.preventDefault();

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    if (users[username] && users[username] === password) {
        // Show the welcome page
        loginPage.style.display = 'none';
        welcomePage.style.display = 'block';
        document.getElementById('username-placeholder').textContent = username;
    } else {
        // Show error message
        errorMessage.style.display = 'block';
    }
});

// Handle "Create Account" link
createAccountLink.addEventListener('click', function() {
    loginPage.style.display = 'none';
    createAccountPage.style.display = 'block';
});

// Handle account creation submission
document.getElementById('createAccountForm').addEventListener('submit', function(e) {
    e.preventDefault();

    const newUsername = document.getElementById('new-username').value;
    const newPassword = document.getElementById('new-password').value;
    const reEnterPassword = document.getElementById('re-enter-password').value;
    const email = document.getElementById('email').value;

    // Validate if passwords match
    if (newPassword !== reEnterPassword) {
        alert("Passwords do not match!");
        return;
    }

    // Add new user to the "database"
    users[newUsername] = newPassword;

    // Show login page after account creation
    alert("Account created successfully! Please log in.");
    createAccountPage.style.display = 'none';
    loginPage.style.display = 'block';
});
