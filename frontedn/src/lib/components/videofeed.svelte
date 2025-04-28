<script>
    import { onMount } from 'svelte';

    // Video feed URL (Flask API route)
    const videoFeedUrl = 'http://127.0.0.1:5001/video_feed'; // Update with your actual Flask API URL

    let videoFrame;

    onMount(() => {
        // Set the src of the image element to the Flask video stream URL
        videoFrame.src = videoFeedUrl;
    });
</script>

<div class="video-container">
    <img alt="Loading video..." class="video-frame" bind:this={videoFrame} />
</div>

<style>
    .video-container {
        width: 100%;
        height: auto;
        display: flex;
        justify-content: center;
        align-items: center;
        background-color: #000;
        border-radius: 8px;
        padding: 10px;
    }

    .video-frame {
        max-width: 100%;
        height: auto;
        border-radius: 6px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.5);
    }
</style>
