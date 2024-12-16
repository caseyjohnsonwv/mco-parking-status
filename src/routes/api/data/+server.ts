import { json, type RequestHandler } from '@sveltejs/kit';
import { parse } from 'node-html-parser';
import { type ParkingLocation } from '$lib/models';


const parkingSiteUrl = 'https://orlandoairports.net/parking-transportation/parking/'


export const GET:RequestHandler = async () => {
    // retrieve table from upstream
    const res = await fetch(parkingSiteUrl);
    console.log(res);
    const bodyText = await res.text();
    console.log(bodyText);
    const upstreamTable = parse(bodyText).getElementsByTagName('section').filter((e) => e.id === 'parking-rates')[0];
    console.log(upstreamTable);
    const upstreamTableCells = upstreamTable.getElementsByTagName('td');

    // convert table to ParkingLocation interfaces
    const parkingLocationsList: ParkingLocation[] = [];
    for (let i = 0; i < upstreamTableCells.length; i += 3) {

        const locationName = upstreamTableCells[i].innerText.trim();
        const daily_rate_usd = upstreamTableCells[i+1].innerText.trim().replace('$', '').toUpperCase().replace('FREE', '0');
        const status = upstreamTableCells[i+2].innerText.trim();

        const parkingLocation: ParkingLocation = {
            name: locationName,
            daily_rate_usd: parseInt(daily_rate_usd),
            status: status.length > 0 ? status.toUpperCase() : 'OPEN',
        };

        parkingLocationsList.push(parkingLocation);
    }

    // return JSON Array
    return json({locations: parkingLocationsList});
}
