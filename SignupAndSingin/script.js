// Elements to update
const confirmPasswordField = document.getElementById('confirm-password');
const nameField = document.getElementById('name');
const formTitle = document.getElementById('form-title');
const formText = document.getElementById('form-text');
const formButton = document.getElementById('form-button');

// Function to switch to login form view
const showLoginView = () => {
    confirmPasswordField.classList.add('hidden');
    nameField.classList.add('hidden');

    formTitle.textContent = 'Login';
    formText.innerHTML = `Don't have an account? <a href="#" id="signup-link" class="link">Sign up</a>`;
    formButton.textContent = 'login';

    // Add event listener to the signupLink to switch to signup view
    const signupLink = document.getElementById('signup-link');
    signupLink.addEventListener('click', (event) => {
        event.preventDefault();
        // Show signup form
        showSignupView();
    });
}

// Function to switch to signup form view
const showSignupView = () => {
    confirmPasswordField.classList.remove('hidden');
    nameField.classList.remove('hidden');

    formTitle.textContent = 'Sign up';
    formText.innerHTML = `Already have an account? <a href="#" id="login-link" class="link">Login</a>`;
    formButton.textContent = 'register';

    // Add event listener to the loginLink to switch to login view
    const loginLink = document.getElementById('login-link');
    loginLink.addEventListener('click', (event) => {
        event.preventDefault();
        // Show login form
        showLoginView();
    });
}


// Call the function to show the login form initially
showLoginView();




// faced some problem with toggling 
// //  Use javascript to select the loginLink element
// const loginLink = document.getElementById('login-link');
// //  Add event listener to the loginLink element
// loginLink.addEventListener('click', (event) => {
//     // Prevent the default behavior of the link
//     event.preventDefault();

    
//     // Elements to hide
//     confirmPasswordField.classList.add('hidden');
//     nameField.classList.add('hidden');

//     // Elements updated
//     formTitle.textContent = 'Login';
//     formText.innerHTML = `Don't have an account? <a href="#" id="signup-link" class="link">Sign up</a>`;
//     formButton.textContent = 'login';

//     // Add event listener to the signupLink element
//     const signupLink = document.getElementById('signup-link');
//     signupLink.addEventListener('click', (event) => {
//         // Prevent the default behavior of the link
//         event.preventDefault();
    
//         // Elements to update
//         const confirmPasswordField = document.getElementById('confirm-password');
//         const nameField = document.getElementById('name');
//         const formTitle = document.getElementById('form-title');
//         const formText = document.getElementById('form-text');
//         const formButton = document.getElementById('form-button');
    
//         // Elements css properties to remove
//         confirmPasswordField.classList.remove('hidden');
//         nameField.classList.remove('hidden');
    
//         // Elements updated
//         formTitle.textContent = 'Sign up';
//         formText.innerHTML = `Already have an account? <a href="#" id="login-link" class="link">Login</a>`;
//         formButton.textContent = 'register';

//         // Re-add event listener for loginLink
//         const loginLink = document.getElementById('login-link');
//         loginLink.addEventListener('click', (event) => {
//             event.preventDefault();

//             confirmPasswordField.classList.add('hidden');
//             nameField.classList.add('hidden');

//             formTitle.textContent = 'Login';
//             formText.innerHTML = `Don't have an account? <a href="#" id="signup-link" class="link">Sign up</a>`;
//             formButton.textContent = 'login';

//             // Re-add event listener for signupLink
//             const signupLink = document.getElementById('signup-link');
//             signupLink.addEventListener('click', (event) => {
//                 event.preventDefault();

//                 confirmPasswordField.classList.remove('hidden');
//                 nameField.classList.remove('hidden');

//                 formTitle.textContent = 'Sign up';
//                 formText.innerHTML = `Already have an account? <a href="#" id="login-link" class="link">Login</a>`;
//                 formButton.textContent = 'register';
//             });
//         });
//     });


// });