<script>
    import { onMount } from 'svelte';
  
    // API configuration for Budapest (Hungary)
    const LATITUDE = 47.4979; // Budapest latitude
    const LONGITUDE = 19.0402; // Budapest longitude
    const API_URL = `https://api.open-meteo.com/v1/forecast?latitude=${LATITUDE}&longitude=${LONGITUDE}&current=temperature_2m,relative_humidity_2m,wind_speed_10m`;
  
    // Reactive variables
    let temperature = 'Loading...';
    let humidity = 'Loading...';
    let wind = 'Loading...';
    let error = null;
    let loading = true;
  
    // Function to fetch weather data
    async function fetchWeather() {
      try {
        console.log('Fetching weather data from:', API_URL); // Log for debugging
        const response = await fetch(API_URL);
        console.log('Response status:', response.status); // Log status
  
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
  
        const data = await response.json();
        console.log('API response:', data); // Log response
  
        // Extract current weather data
        const current = data.current;
        temperature = `${Math.round(current.temperature_2m)}°C`;
        humidity = `${current.relative_humidity_2m}%`;
        wind = `${Math.round(current.wind_speed_10m)} km/h`;
        error = null;
      } catch (err) {
        console.error('Error fetching weather:', err);
        error = `Failed to fetch weather data: ${err.message}`;
        temperature = humidity = wind = 'N/A';
      } finally {
        loading = false;
      }
    }
  
    // Fetch data on mount
    onMount(() => {
      fetchWeather();
      return () => {}; // Cleanup if needed
    });
  </script>
  
  <div class="weather-widget">
    {#if loading}
      <p>Loading weather data...</p>
    {:else if error}
      <p>Error: {error}</p>
    {:else}
      <p>Current Weather: <span>{temperature}</span></p>
      <p>Humidity: <span>{humidity}</span></p>
      <p>Wind: <span>{wind}</span></p>
    {/if}
  </div>
  
  <style>
    /* Weather Widget */
    .weather-widget {
      background-color: #1c1c1c;
      border-radius: 8px;
      padding: 10px;
      margin: 20px 0;
      display: flex;
      justify-content: space-between;
      align-items: center;
      box-shadow: 0 2px 10px rgba(152, 188, 152, 0.2);
    }
  
    .weather-widget p {
      margin: 0;
      color: #33ff33;
    }
  
    .weather-widget span {
      font-weight: bold;
      color: #1aff1a;
    }
  </style>