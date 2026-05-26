# Travel Budget Explorer: Design & Implementation

## Overview
The **Travel Budget Explorer** is a static site that helps users discover travel destinations based on their budget and departure date. This document outlines the design decisions, challenges, and future roadmap.

## Motivation
- **Problem**: Many travel websites focus on specific destinations rather than helping users explore options within their budget.
- **Solution**: A minimalist tool that filters destinations based on user input (budget, departure date).

## Design Decisions
### 1. Static Site
- **Why**: Reduces backend complexity and hosting costs.
- **Trade-offs**: Limited to client-side logic (e.g., no server-side API calls).

### 2. Mock Data
- **Why**: Avoids rate limits and API restrictions during development.
- **Trade-offs**: Data is static and may become outdated.

### 3. Bootstrap
- **Why**: Provides responsive design out-of-the-box.
- **Trade-offs**: Limited customization without additional CSS.

### 4. Client-Side Filtering
- **Why**: Enables dynamic results without a backend.
- **Trade-offs**: Performance may degrade with large datasets.

## Challenges
### 1. API Restrictions
- **Issue**: Flight APIs (e.g., Skyscanner, Kiwi) require authentication and have rate limits.
- **Solution**: Use mock data for prototyping; integrate APIs in future iterations.

### 2. Local Testing
- **Issue**: `python3 -m http.server` may conflict with existing processes.
- **Solution**: Kill conflicting processes before restarting the server.

### 3. GitHub Publishing
- **Issue**: Namespace mismatches may prevent repository creation.
- **Solution**: Use `fairyfemirins` as a fallback namespace and document the transfer process.

## Roadmap
1. **API Integration**: Replace mock data with a real flight API.
2. **User Accounts**: Add localStorage to save user preferences.
3. **Deployment**: Host on GitHub Pages for free.
4. **Filters**: Add options for continent, climate, and duration.

## License
MIT