<script lang="ts">
    import ParkingStatus from "./ParkingStatus.svelte";

    export let locations: {name:string, status:string, daily_rate_usd:number}[];
</script>

<div class="mx-auto max-w-4xl space-y-3 p-3 bg-zinc-300 text-zinc-900 rounded-sm">
    <p class="text-2xl text-center font-semibold"><slot/></p>
    {#each locations as locationProps}
        <ParkingStatus props={locationProps}/>
    {/each}
</div>
