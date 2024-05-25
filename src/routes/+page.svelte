<script lang="ts">
    import { onMount } from "svelte";
    import moment_timezone from "moment-timezone";
    import LocationList from "./LocationList.svelte";

    let refreshTimestamp: string;
    let locations: {name:string, status:string, dailyRateUSD:number}[];

    $: garageLocations = locations ? locations.filter((v) => (v.name.toLowerCase().includes('garage') || v.name.toLowerCase().includes('terminal top'))).sort((a,b) => (a.name.localeCompare(b.name))) : [];
    $: economyLocations = locations ? locations.filter((v) => (v.name.toLowerCase().includes('economy'))).sort((a,b) => (a.name.localeCompare(b.name))) : [];
    $: valetLocations = locations ? locations.filter((v) => (v.name.toLowerCase().includes('valet') && !v.name.toLowerCase().includes('hotel'))).sort((a,b) => (a.name.localeCompare(b.name))) : [];
    $: surfaceLocations = locations ? locations.filter((v) => (v.name.toLowerCase().includes('surface'))).sort((a,b) => (a.name.localeCompare(b.name))) : [];

    onMount(() => {
        fetch('/api/data').then((res) => res.json().then((j) => {
            locations = j.locations
        }))
        .catch((err) => console.error(err));
        
        refreshTimestamp = moment_timezone().tz('America/New_York').format('h:mm a');
    });
</script>

<div class="bg-zinc-900 text-zinc-200">
    <div class="mx-auto max-w-xl w-screen min-h-screen px-4 py-10 justify-center space-y-2">
        <p class="text-center space-y-3 font-light text-3xl">MCO Parking Status</p>
        <div class="space-y-5 text-center">
            {#if locations}
                <p class="text-center text-xs">Refreshed at <span class="px-1.5 mx-0.5 rounded-sm bg-blue-800 font-medium">{refreshTimestamp.toUpperCase()}</span> Orlando time.</p>
                <div class="space-y-5">
                    <LocationList locations={economyLocations}>
                        <span slot="title">Economy Lots</span>
                        <span slot="payment">Cash, card, or E-Pass/SunPass</span>
                    </LocationList>
                    <LocationList locations={surfaceLocations}>
                        <span slot="title">Surface Lots</span>
                        <span slot="payment">E-Pass/SunPass ONLY</span>
                    </LocationList>
                    <LocationList locations={garageLocations}>
                        <span slot="title">Garages</span>
                        <span slot="payment">Cash, card, or E-Pass/Sunpass</span>
                    </LocationList>
                    <LocationList locations={valetLocations}>
                        <span slot="title">Valets</span>
                        <span slot="payment">Cash or card ONLY. Open 6:00am - 11:00pm</span>
                    </LocationList>
                </div>
                <div class="space-y-3">
                    <div class="font-semibold max-w-64 mx-auto bg-zinc-100 text-zinc-900 p-1 pt-1.5 rounded-sm">
                        <a href="https://orlandoairports.net/parking-transportation/parking/" target="_blank" class="flex flex-row justify-center space-x-2 items-center text-sm">
                            <span>View on MCO website</span>
                            <i class="fa-solid fa-arrow-up-right-from-square text-xs"></i>
                        </a>
                    </div>
                    <div class="font-light max-w-64 mx-auto bg-blue-800 text-zinc-50 p-1 pt-1.5 rounded-sm">
                        <a href="https://linkedin.com/in/caseyjohnsonwv" target="_blank" class="flex flex-row justify-center space-x-2 items-baseline text-sm">
                            <span>Created by Casey Johnson</span>
                            <i class="fa-brands fa-linkedin text-lg"></i>
                        </a>
                    </div>
                </div>
                <hr>
                <div>
                    <a href="https://venmo.com/u/caseyjohnsonwv" target="_blank">
                        <div class="bg-zinc-800 text-zinc-400 text-sm flex flex-col justify-center text-center p-2 rounded-md">
                            <span class="font-semibold mb-2">This page costs $97/year to operate.</span>
                            <span class="font-light">Domain name registration: $13/year.</span>
                            <span class="font-light">Server: $84/year (billed monthly for $7).</span>
                            <span class="font-medium mt-2 underline">Donations welcome via Venmo!</span>
                        </div>
                    </a>
                </div>
            {:else}
                <div class="space-y-8">
                    <p class="text-xs text-zinc-200">Refreshing...</p>
                    <i class="fa-solid fa-spinner animate-spin"></i>
                </div>
            {/if}
        </div>
    </div>
</div>
