# Flight Deals  
Flight Deals is a Python application that automates flight searches using the **Tequila API (Kiwi.com)**. When a suitable deal is found, it sends **email or SMS notifications**, allowing users to stay informed about the best flight prices.  

## Demo Video  
Watch the project in action!: **[FlightDeals Demo on YouTube](https://youtu.be/xnj6AMYMrZo)**  

### Automated Flight Search  
The application scans available flights based on predefined parameters. If a matching flight is found, it sends an **SMS notification** with flight details and a direct booking link.  

### User Subscription System  
Users can **subscribe to receive email alerts** whenever a flight deal is found. The email includes **departure and arrival details, pricing, and a direct booking link**.  

### Smart Data Management  
The program integrates with **Google Sheets**, where it stores primary city names and historical lowest ticket prices. It also **automatically retrieves missing IATA codes** and filters flights within a specified date range, from tomorrow up to six months ahead.  

## Key Technologies Used  
- **Tequila API (Kiwi.com)** – Flight search  
- **Sheety API** – Google Sheets integration  
- **Twilio API** – SMS notifications  

## Installation & Setup  
This project requires handling sensitive environment variables (`.env`) and API keys. Setting it up involves registering API access and configuring your environment accordingly.  

For those interested in implementation details or a demonstration, a **walkthrough can be provided upon request**.  
