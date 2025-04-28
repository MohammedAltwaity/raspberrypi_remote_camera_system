<style>
    :root {
      --primary-color: #33ff33;
      --background-color: #000000;
      --secondary-bg: #121212;
      --text-color: #ffffff;
      --shadow-color: rgba(51, 255, 51, 0.2);
    }
  
    .welcome-container {
      text-align: center;
      padding: 40px;
      background-color: var(--secondary-bg);
      border-radius: 12px;
      box-shadow: 0 6px 15px var(--shadow-color);
      width: 100%;
      max-width: 500px;
      margin: 20px auto;
      font-family: 'Arial', sans-serif;
      opacity: 0;
      animation: fadeIn 0.6s ease-out forwards;

      margin-top: 80px;
    }
  
    @keyframes fadeIn {
      from { opacity: 0; }
      to { opacity: 1; }
    }
  
    .welcome-container h1 {
      margin: 0 0 25px;
      font-size: 2.2rem;
      color: var(--primary-color);
      text-transform: uppercase;
      letter-spacing: 1.5px;
    }
  
    .welcome-container a {
      display: inline-block;
      margin-top: 15px;
      padding: 12px 30px;
      font-size: 1.1rem;
      font-weight: 600;
      color: var(--text-color);
      background: linear-gradient(135deg, #000000 0%, #1a1a1a 100%);
      text-decoration: none;
      border-radius: 8px;
      transition: background 0.3s ease, transform 0.2s ease;
    }
  
    .welcome-container a:hover {
      background: linear-gradient(135deg, #1a1a1a 0%, #333333 100%);
      transform: translateY(-2px);
    }
  
    .welcome-container a:active {
      transform: translateY(0);
    }
  
    @media (max-width: 600px) {
      .welcome-container {
        padding: 20px;
        margin: 10px;
      }
  
      .welcome-container h1 {
        font-size: 1.8rem;
      }
  
      .welcome-container a {
        padding: 10px 20px;
        font-size: 1rem;
      }
    }
  </style>
  
  <div class="welcome-container">
    <h1>Welcome</h1>
    <a href="/login">Login</a>
  </div>