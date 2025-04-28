<script>

import "$lib/styles/global.css"
import Welcome from "$lib/components/welcome.svelte"; 
import { goto } from '$app/navigation';
  // Redirect after component mount
import { onMount } from 'svelte';
  import Footer from "$lib/components/footer.svelte";
  
    // onMount(() => {
    //   goto('/home');
    // });


  </script>
  <main>
  <Welcome/>
</main>

<footer>

<Footer/>
</footer>
<style>

  main{
    margin-top: 20px;
    margin-bottom: 40px;
  }
  footer{
    margin-top: 300px;
  }
</style>


  