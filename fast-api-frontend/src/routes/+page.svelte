<script>
	// Function to fetch data from backend
	async function getData() {
		const res = await fetch("http://localhost:8000/blah"); // replace with your actual backend URL

		if (!res.ok) {
			// If response is not ok, get text and throw as error
			const text = await res.text();
			throw new Error(text);
		}

		// Parse response as JSON
		return await res.json();
	}

	// Initial promise
	let promise = getData();

	// Function to re-fetch data on button click
	function handleClick() {
		promise = getData();
	}
</script>

<h1>Welcome to SvelteKit</h1>

<p>
	Visit
	<a href="https://svelte.dev/docs/kit" target="_blank">
		svelte.dev/docs/kit
	</a>
	to read the documentation
</p>

<button on:click={handleClick}>
	Get Data
</button>

<!-- Async block to handle promise -->
{#await promise}
	<p>...waiting</p>
{:then data}
	<p>Data is {data.hello}</p>
{:catch error}
	<p style="color: red;">Error is {error.message}</p>
{/await}
