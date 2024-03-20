// Example: Prevent form submission if address is invalid
function validateAddress(event) {
    const addressInput = document.querySelector('input[name="address"]');
    const address = addressInput.value.trim();

    // Perform basic validation for Ethereum addresses
    if (!address.startsWith('0x') || address.length !== 42) {
        event.preventDefault();
        alert('Please enter a valid Ethereum address.');
    }
}

// Attach event listener to vote form
const voteForm = document.querySelector('form[action="/vote"]');
if (voteForm) {
    voteForm.addEventListener('submit', validateAddress);
}