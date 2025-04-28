<script>
    import WeatherWidget from "$lib/components/wetherwidget.svelte";
    import VideoFeed from "$lib/components/videofeed.svelte";
    import ConfigPanel from "$lib/components/configpanel.svelte";
</script>

<div class="main-container">
    <WeatherWidget />
    <div class="content">
        <VideoFeed />
        <ConfigPanel />
    </div>
</div>

<style>
    .main-container {
        display: flex;
        flex-direction: column;
        padding: 20px;
        gap: 20px;
    }

    .content {
        display: flex;
        gap: 20px;
    }
</style>
