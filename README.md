# Travel Budget Explorer

A web app to discover travel destinations based on your flight budget and date.

## Features
- Enter your departure airport, travel date, and budget to see destinations you can afford.
- Results include flight price, airline, departure/arrival times, and a booking link.
- Sortable by continent, region, or climate (planned).

## Tech Stack
- **Frontend**: HTML, CSS, JavaScript (Bootstrap)
- **Backend**: Python (Flask) + SQLite (for caching)
- **API**: Kiwi API (flight pricing)

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/femirins/travel-budget-explorer.git
   cd travel-budget-explorer
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. Run the Flask app:
   ```bash
   python app.py
   ```

4. Open your browser and navigate to `http://127.0.0.1:5000`.

## Configuration
- Replace `your_kiwi_api_key` in `app.py` with your actual Kiwi API key.
- Configure SQLite database for caching flight data.

## License
MIT