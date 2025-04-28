<script>
 import "$lib/styles/global.css";
 import Navigation from "$lib/components/navigation.svelte";
 import Footer from "$lib/components/footer.svelte";

</script>

<header>

    <Navigation/>
   
</header>

<main>

    <slot></slot>
</main>


<footer>
<Footer/>
</footer>