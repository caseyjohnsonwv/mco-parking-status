<script lang="ts">
    import { env } from "$env/dynamic/public";
    import { onMount } from "svelte";
    import moment_timezone from "moment-timezone";
    import LocationList from "./LocationList.svelte";

    let refreshTimestamp: string;
    let locations: {name:string, status:string, daily_rate_usd:number, last_updated_datetime:string}[];

    $: garageLocations = locations ? locations.filter((v) => (v.name.toLowerCase().includes('garage') || v.name.toLowerCase().includes('terminal top'))).sort((a,b) => (a.name.localeCompare(b.name))) : [];
    $: economyLocations = locations ? locations.filter((v) => (v.name.toLowerCase().includes('economy'))).sort((a,b) => (a.name.localeCompare(b.name))) : [];
    $: valetLocations = locations ? locations.filter((v) => (v.name.toLowerCase().includes('valet') && !v.name.toLowerCase().includes('hotel'))).sort((a,b) => (a.name.localeCompare(b.name))) : [];
    $: surfaceLocations = locations ? locations.filter((v) => (v.name.toLowerCase().includes('surface'))).sort((a,b) => (a.name.localeCompare(b.name))) : [];


    onMount(() => {
        fetch(`${env.PUBLIC_API_BASE_URL}/mco/`)
            .then((res) => res.json().then((j) => locations = j.locations))
            .catch((err) => console.error(err))
        ;

        refreshTimestamp = moment_timezone().tz('America/New_York').format('h:mm a');
    });
</script>

<div class="bg-zinc-900 text-zinc-200">
    <div class="mx-auto max-w-4xl w-screen min-h-screen px-4 py-10 justify-center space-y-7">
        {#if locations}
            <div class="text-center space-y-3 font-light">
                <p class="text-3xl">MCO Parking Status</p>
                <p class="text-xs">Refreshed at <span class="px-1.5 mx-0.5 rounded-sm bg-blue-800 font-medium">{refreshTimestamp.toUpperCase()}</span> Orlando time.</p>
            </div>
            <div class="space-y-5">
                <LocationList locations={economyLocations}>Economy Lots</LocationList>
                <LocationList locations={surfaceLocations}>Surface Lots</LocationList>
                <LocationList locations={garageLocations}>Garages</LocationList>
                <LocationList locations={valetLocations}>Valets</LocationList>
            </div>
            <div class="space-y-3">
                <div class="font-semibold max-w-64 mx-auto bg-zinc-100 text-zinc-900 p-1 pt-1.5 rounded-sm">
                    <a href="https://orlandoairports.net/parking-transportation/parking/" target="_blank" class="flex flex-row justify-center space-x-2 items-center text-sm">
                        <span>View on MCO website</span>
                        <i class="fa-solid fa-arrow-up-right-from-square text-xs"></i>
                    </a>
                </div>
                <div class="font-light max-w-64 mx-auto bg-blue-800 text-zinc-50 p-1 pt-1.5 rounded-sm">
                    <a href="https://linkedin.com/in/caseyjohnsonwv" target="_blank" class="flex flex-row justify-center space-x-3 items-baseline text-sm">
                        <span>Created by Casey Johnson</span>
                        <i class="fa-brands fa-linkedin text-lg"></i>
                    </a>
                </div>
            </div>
        {:else}
            <div class="text-center font-light mt-24">
                <i class="fa-solid fa-spinner animate-spin"></i>
            </div>
        {/if}
    </div>
</div>
