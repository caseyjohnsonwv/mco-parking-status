<script lang="ts">
    export let props: {name:string, status:string, dailyRateUSD:number};

    $: isOpen = props.status.toLowerCase() === 'open';
</script>

<div class="flex flex-row align-middle items-center justify-between text-xs font-semibold {isOpen ? 'bg-green-500' : 'bg-red-600'} py-1 px-2 rounded-sm">
    <div class="w-2/3 text-left">
        {props.name}
    </div>
    <div class="flex flex-row align-middle items-center space-x-5 w-1/3 justify-end">
        <span>{props.status}</span>
        <span>${props.dailyRateUSD}/day</span>
    </div>
</div>
