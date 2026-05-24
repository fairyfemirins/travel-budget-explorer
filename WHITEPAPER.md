# Travel Budget Explorer: Design Decisions & Challenges

## 🎯 Problem Statement
- **Demand**: 439 upvotes on [r/SomebodyMakeThis](https://www.reddit.com/r/SomebodyMakeThis/comments/bnp9f) for a tool that helps users discover affordable travel destinations.
- **Gap**: No open-source tool exists for this exact use case.

## 🛠️ Design Decisions

### 1. Tech Stack
| Component       | Choice               | Rationale                                                                                     |
|----------------|----------------------|-----------------------------------------------------------------------------------------------|
| Backend        | Flask (Python)       | Lightweight, easy to deploy, and integrates well with APIs.                                  |
| Frontend       | Bootstrap 5 + JS     | Responsive design with minimal dependencies.                                                 |
| Data           | Mock JSON            | Fallback for API restrictions (e.g., Skyscanner, Kiwi).                                      |
| Deployment     | Docker (optional)    | Self-hosting support for users without cloud access.                                         |

### 2. Mock Data Integration
- **Why**: External APIs (e.g., Skyscanner, Kiwi) are often rate-limited or blocked.
- **How**: Hardcoded JSON with 3 destinations (Paris, Tokyo, New York).
- **Future**: Replace with real API calls (e.g., Skyscanner API).

### 3. User Experience
- **Input**: Budget ($) + Departure Date (required fields).
- **Output**: Cards with destination name, price, airline, and image.
- **Error Handling**: Alerts for no results (e.g., "Try increasing your budget").

## 🔥 Challenges & Solutions

### 1. API Restrictions
- **Problem**: Skyscanner/Kiwi APIs require approval or are rate-limited.
- **Solution**: Mock data for prototyping. See [`app/app.py`](app/app.py) for the fallback.

### 2. Deployment
- **Problem**: Flask’s development server is not production-ready.
- **Solution**: Docker setup for self-hosting (see `Dockerfile`).

### 3. Responsiveness
- **Problem**: Bootstrap 5 may not fit all screen sizes perfectly.
- **Solution**: Custom CSS for mobile-friendly cards (see `templates/index.html`).

## 📈 Future Improvements
- **Real API Integration**: Replace mock data with Skyscanner/Kiwi API.
- **User Accounts**: Save favorite destinations.
- **Filters**: Add options for continent, climate, or airline.
- **Deployment**: Add support for Vercel/Heroku.

## 📜 License
MIT License. See [LICENSE](LICENSE) for details.