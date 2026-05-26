// Mock flight data
const MOCK_DESTINATIONS = [
    {
        destination: "Paris",
        price: 200,
        departure_date: "2026-12-01",
        airline: "Air France",
        image_url: "https://images.unsplash.com/photo-1502602898536-47ad22581b52?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1470&q=80"
    },
    {
        destination: "Tokyo",
        price: 500,
        departure_date: "2026-12-01",
        airline: "Japan Airlines",
        image_url: "https://images.unsplash.com/photo-1540959733332-eab4deabeeaf?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1653&q=80"
    },
    {
        destination: "Barcelona",
        price: 300,
        departure_date: "2026-12-01",
        airline: "Iberia",
        image_url: "https://images.unsplash.com/photo-1539037116277-4db20889f2d4?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1470&q=80"
    },
    {
        destination: "Bangkok",
        price: 400,
        departure_date: "2026-12-01",
        airline: "Thai Airways",
        image_url: "https://images.unsplash.com/photo-1563492065599-3520f775eeed?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1470&q=80"
    },
    {
        destination: "New York",
        price: 150,
        departure_date: "2026-12-01",
        airline: "Delta",
        image_url: "https://images.unsplash.com/photo-1496442226666-8d4d0e62e6e9?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1470&q=80"
    }
];

// Handle form submission
document.getElementById('search-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const budget = parseFloat(document.getElementById('budget').value);
    const departureDate = document.getElementById('departure-date').value;

    // Filter destinations based on budget and departure date
    const results = MOCK_DESTINATIONS.filter(dest => {
        return dest.price <= budget && dest.departure_date === departureDate;
    });

    // Display results
    const resultsContainer = document.getElementById('results-container');
    resultsContainer.innerHTML = '';

    if (results.length === 0) {
        resultsContainer.innerHTML = `
            <div class="col-12">
                <div class="alert alert-info text-center">
                    No destinations found for your budget and departure date.
                </div>
            </div>
        `;
    } else {
        results.forEach(dest => {
            resultsContainer.innerHTML += `
                <div class="col-md-4">
                    <div class="card">
                        <img src="${dest.image_url}" class="card-img-top" alt="${dest.destination}">
                        <div class="card-body">
                            <h5 class="card-title">${dest.destination}</h5>
                            <p class="card-text">
                                <strong>Price:</strong> $${dest.price}<br>
                                <strong>Airline:</strong> ${dest.airline}<br>
                                <strong>Departure:</strong> ${dest.departure_date}
                            </p>
                        </div>
                    </div>
                </div>
            `;
        });
    }
});