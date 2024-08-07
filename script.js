const form = document.getElementById('donation-form');
const paymentGateway = document.getElementById('payment-gateway');

form.addEventListener('submit', (e) => {
    e.preventDefault();
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const phone = document.getElementById('phone').value;
    const organization = document.getElementById('organization').value;
    const donationAmount = document.getElementById('donation-amount').value;

    // Razorpay payment gateway integration
    const razorpayOptions = {
        key: 'YOUR_RAZORPAY_KEY', // Replace with your Razorpay key
        amount: donationAmount * 100, // Convert to paise
        currency: 'INR',
        name: 'Pad Donation Website',
        description: 'Donation to Pad Donation Website',
        image: 'https://example.com/image.jpg', // Replace with your logo image
        handler: function(response) {
            // Handle payment success
            console.log(response);
            alert('Payment successful!');
        },
        prefill: {
            name: name,
            email: email,
            contact: phone,
        },
        notes: {
            organization: organization,
        },
        theme: {
            color: '#4CAF50',
        },
    };

    const razorpayCheckout = new Razorpay(razorpayOptions);
    razorpayCheckout.open();
});