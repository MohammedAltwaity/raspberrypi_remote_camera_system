<script>
      import { onMount } from 'svelte';

let userId = '';
let address = '';
let errorMessage = ''; // Used to display errors to the user

// Fetch user information on component mount
onMount(async () => {
    try {
        const response = await fetch('http://127.0.0.1:5001/get_user_info', {
            method: 'GET',
            credentials: 'include', // Ensure cookies are sent with the request
        });

        if (response.ok) {
            const data = await response.json();
            console.log('User Information:', data);

            // Assign user info to variables
            userId = data.user_info.userid;
            address = data.user_info.name; // Assuming "name" is the address field; adjust if necessary
        } else {
            // Handle errors if the response status is not OK
            const errorData = await response.json();
            errorMessage = errorData.message || 'Failed to fetch user information.';
            console.error('Error fetching user info:', errorMessage);
        }
    } catch (error) {
        // Handle network errors
        console.error('Network error:', error);
        errorMessage = 'Unable to connect to the server. Please try again later.';
    }
});


</script>

<div class="config-panel">
    <h3>User Information</h3>

    <!-- Display User Info -->
    <div class="user-info">
        <p><strong>User ID:</strong> {userId}</p>
        <p><strong>Address:</strong> {address}</p>
    </div>
</div>

<style>
    /* Configuration Panel Styles */
    .config-panel {
        width: 250px;
        background-color: #121212;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 2px 10px rgba(0, 255, 0, 0.2);
        height: 100%;
    }

    .config-panel h3 {
        margin-bottom: 15px;
        color: #33ff33;
    }

    .config-panel label {
        display: block;
        margin-bottom: 10px;
    }

    /* User Info Styles */
    .user-info {
        margin-bottom: 20px;
        color: #33ff33;
    }

    .user-info p {
        margin: 5px 0;
        font-size: 14px;
    }
</style>
