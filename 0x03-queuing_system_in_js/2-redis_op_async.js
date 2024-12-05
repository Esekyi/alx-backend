import { createClient, print } from "redis";
import { promisify } from "util";

const client = createClient();


client.on("error", err => console.log('Redis client not connected to the server:', err))
	.on('connect', () => console.log('Redis client connected to the server'));


function setNewSchool(schoolName, value)
{
	client.set(schoolName, value, print);
}

async function displaySchoolValue(schoolName)
{
	const asyncGet = promisify(client.get).bind(client);
	const res = await asyncGet(schoolName);
	console.log(res);
}


await displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
await displaySchoolValue('HolbertonSanFrancisco');
