<script lang="ts">
    import ParkingStatus from "./ParkingStatus.svelte";

    export let locations: {name:string, status:string, dailyRateUSD:number}[];
</script>

<div class="mx-auto max-w-4xl space-y-4 p-3 bg-zinc-300 text-zinc-900 rounded-sm">
    <div class="text-center space-y-0.5">
        <p class="text-2xl font-semibold"><slot name="title"/></p>
        <p class="text-xs"><slot name="payment"/></p>
    </div>
    <div class="space-y-3">
        {#each locations as locationProps}
            <ParkingStatus props={locationProps}/>
        {/each}
    </div>
</div>
