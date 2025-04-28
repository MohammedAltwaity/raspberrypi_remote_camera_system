<script>
    // Redirect to login page on button click
    const redirectToLogin = () => {
        window.location.href = '/login'; // Adjust the path if your login page URL is different
    };
</script>

<style>
    .logout-container {
        max-width: 400px;
        margin: 50px auto;
        padding: 30px;
        background-color: #121212;
        border-radius: 12px;
        box-shadow: 0 8px 20px rgba(51, 255, 51, 0.2);
        width: 100%;
        text-align: center;
        overflow: hidden;
    }

    h1 {
        color: #33ff33;
        margin-bottom: 25px;
        font-size: 2rem;
        text-transform: uppercase;
        letter-spacing: 2px;
    }

    p {
        color: #ffffff;
        margin-bottom: 20px;
        font-size: 1rem;
    }

    .logout-btn {
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

    .logout-btn:hover {
        background-color: #1aff1a;
    }
</style>

<main class="logout-container">
    <h1>Logged Out</h1>
    <p>You have successfully logged out. Thank you for visiting!</p>
    <button class="logout-btn" on:click={redirectToLogin}>Return to Login</button>
</main>
