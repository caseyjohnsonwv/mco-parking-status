<script lang="ts">
    import "../app.css";
    import '@fortawesome/fontawesome-free/css/all.min.css';
    import { page } from "$app/stores";

    const faviconPath = `${$page.url.host}/favicon.png`
</script>

<svelte:head>
    <meta property="og:image" content={faviconPath} />
</svelte:head>

<slot />
