# Travel Budget Explorer

**Reverse budget search for flights.**
Enter your departure city, travel date, and budget — get a list of destinations you can afford, sorted by price, continent, or climate.

![Demo](docs/demo.gif)

## Features
- Input: Departure city, date, budget.
- Output: Destinations under budget, with price, continent, and climate.
- Sorting: Price, continent, climate.
- Data: SQLite (mock data for now; Kiwi API planned).

## Quickstart
```bash
# Clone
git clone https://github.com/femirins/travel-budget-explorer.git
cd travel-budget-explorer

# Install
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run
python3 app.py
```

Open [http://localhost:5000](http://localhost:5000) in your browser.

## Technical Architecture
- **Backend:** Flask (Python), SQLite.
- **Frontend:** Bootstrap 5, vanilla JS.
- **Data:** Mock flights (NYC → Paris, Tokyo, Bangkok, Sydney, Cape Town).
- **API:** `/search?departure=NYC&date=2026-12-01&budget=700` → JSON.

## Roadmap
- [ ] Integrate Kiwi API for real-time flight data.
- [ ] User accounts (save searches, alerts).
- [ ] Climate/continent filters.

## License
MIT