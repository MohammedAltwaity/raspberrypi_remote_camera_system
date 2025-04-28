<script>
   
   import "$lib/styles/global.css";

let id = '';
let password = '';
let errorMessage = '';

const handleSubmit = async (event) => {
    event.preventDefault(); // Prevent form submission from reloading the page

    try {
        const response = await fetch('http://127.0.0.1:5001/login', { // Flask login API
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ id, password }),
            credentials: 'include',  // Ensure session cookies are included in the request
        });

        // If the response is OK, process the login success
        if (response.ok) {
            const data = await response.json();
            console.log('Login successful:', data);

            // Extract the Set-Cookie header if present
            const setCookieHeader = response.headers.get('set-cookie');
            if (setCookieHeader) {
                console.log('Set-Cookie:', setCookieHeader); // Debug: Log the Set-Cookie header
            }

            // Store the user ID in localStorage
            localStorage.setItem('user_id', id); // Save the logged-in user's ID

            // Redirect to the home page
            window.location.href = '/home';
        } else {
            const errorData = await response.json();
            errorMessage = errorData.message || 'An error occurred during login';
        }
    } catch (error) {
        console.error('Error:', error);
        errorMessage = 'Network error, please try again later';
    }
};




</script>

<style>
    .login-container {
        max-width: 400px;
        margin: 50px auto;
        padding: 30px;
        background-color: #121212;
        border-radius: 12px;
        box-shadow: 0 8px 20px rgba(51, 255, 51, 0.2);
        width: 100%;
        overflow: hidden;
    }

    h1 {
        text-align: center;
        color: #33ff33;
        margin-bottom: 25px;
        font-size: 2rem;
        text-transform: uppercase;
        letter-spacing: 2px;
    }

    .error {
        color: #ff3333;
        text-align: center;
        margin-bottom: 15px;
        font-size: 0.9rem;
        padding: 8px;
        background-color: #1c1c1c;
        border-radius: 4px;
    }

    .login-form {
        display: flex;
        flex-direction: column;
        gap: 20px;
    }

    .input-group {
        display: flex;
        flex-direction: column;
        gap: 5px;
    }

    label {
        margin-bottom: 5px;
        font-weight: 600;
        color: #33ff33;
        text-transform: uppercase;
        font-size: 0.9rem;
        letter-spacing: 1px;
    }

    input {
        padding: 12px;
        border: 2px solid #33ff33;
        border-radius: 8px;
        font-size: 1rem;
        background-color: #1c1c1c;
        color: #33ff33;
        transition: border-color 0.3s ease, box-shadow 0.3s ease;
    }

    input:focus {
        border-color: #1aff1a;
        box-shadow: 0 0 10px rgba(51, 255, 51, 0.5);
        outline: none;
    }

    input::placeholder {
        color: #66ff66;
        opacity: 0.7;
    }

    .login-btn {
        padding: 12px;
        background-color: #33ff33;
        color: #000000;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        font-size: 1.1rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
        transition: background-color 0.3s ease;
    }

    .login-btn:hover {
        background-color: #1aff1a;
    }
</style>

<main class="login-container">
    <h1>Login</h1>
    {#if errorMessage}
        <p class="error">{errorMessage}</p>
    {/if}
    <form class="login-form" on:submit={handleSubmit}>
        <div class="input-group">
            <label for="id">ID</label>
            <input
                type="text"
                id="id"
                bind:value={id}
                placeholder="Enter your ID"
                required
            />
        </div>
        <div class="input-group">
            <label for="password">Password</label>
            <input
                type="password"
                id="password"
                bind:value={password}
                placeholder="Enter your password"
                required
            />
        </div>
        <button type="submit" class="login-btn">Login</button>
    </form>
</main>
