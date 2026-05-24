# Travel Budget Explorer

**Find affordable travel destinations within your budget.**

![Screenshot](https://i.imgur.com/XYZ1234.png)

## 🚀 Features
- Enter your **budget** and **departure date** to discover destinations you can afford.
- Results include **destination name, price, airline, and images**.
- **Responsive design** (works on mobile and desktop).
- **Mock data** for testing (fallback for API restrictions).

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- pip

### Setup
```bash
git clone https://github.com/fairyfemirins/travel-budget-explorer.git
cd travel-budget-explorer
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

### Run
```bash
python app/app.py
```
Open [http://localhost:5000](http://localhost:5000) in your browser.

## 📂 Project Structure
```
├── app/
│   ├── static/             # CSS, JS, images
│   ├── templates/          # HTML templates
│   │   └── index.html      # Homepage
│   └── app.py             # Flask backend
├── README.md              # Project overview
├── WHITEPAPER.md          # Design decisions
└── LICENSE                # MIT License
```

## 🔧 Technical Architecture
- **Backend**: Flask (Python)
- **Frontend**: Bootstrap 5 + Vanilla JS
- **Data**: Mock JSON (fallback for API restrictions)
- **Deployment**: Docker (optional)

## 🤝 Contributing
Contributions are welcome! Open an issue or submit a pull request.

## 📜 License
MIT License. See [LICENSE](LICENSE) for details.