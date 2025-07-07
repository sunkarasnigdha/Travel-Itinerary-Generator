## [Travel Itinerary Generator Using AI](Travel-Itinerary-Generator-Using-AI)


<img title="Travel-Itinerary-Generator-Using-AI" align='right' src="/static/logo.png" alt="Travel Itinerary Generator Logo" width="150"/>

Plan your dream trip effortlessly with the Travel Itinerary Generator! This powerful trip planner is your ultimate companion for crafting seamless travel experiences. Whether you're embarking on a road trip, city excursion, or overseas adventure, our tool simplifies the entire planning process.
## Sample:





<p align="center">
Make your travel dreams a reality. Start planning your next adventure with the Travel Itinerary Generator today!
</p>
<p align="center">
<i>Explore, discover, and make every trip unforgettable.*</i>
</p>

## Table of Contents

- [Travel Itinerary Generator Using AI](#travel-itinerary-generator-using-ai)
  - [Sample:](#sample)
  - [Table of Contents](#table-of-contents)
  - [About](#about)
  - [Limitations \& Future Work](#limitations--future-work)
  - [Features](#features)
  - [Requirements](#requirements)
  - [Setup and Installation](#setup-and-installation)
  - [API Keys](#api-keys)
  - [Usage](#usage)
  - [Screenshots](#screenshots)
  - [License](#license)

## About

Travel Itinerary Generator is a computer program that empowers travelers to effortlessly create personalized travel itineraries. By considering users' interests, budgets, and travel dates, this application generates comprehensive lists of activities, attractions, and accommodations. Whether you're an experienced traveler or a novice, the Travel Itinerary Generator is your key to saving time and ensuring an enriching and well-rounded travel experience.

## Limitations & Future Work
- The Travel Itinerary Generator works only based on the user's source and destination and time of travel.

***Future Work***
- The Travel Itinerary Generator is not able to generate itineraries for multiple destinations.
- The Travel Itinerary Generator is not able to suggest hotels and flights.
- **Real-time Collaboration:** In an increasingly interconnected world, we plan to introduce real-time collaboration features. Users will be able to share their itineraries with travel companions or collaborators, making group travel planning an effortless and collaborative experience.

## Features

- **Weather Forecast:** The Travel Itinerary Generator provides a weather forecast of the destination for the whole travel time.
- **Travel Itinerary:** The Travel Itinerary Generator provides a travel itinerary for the whole travel time in an optimum budget.
- **Translation Feature:** The Travel Itinerary Generator Using AI provides a translation feature to help users to communicate in the destination's language.
## Requirements

- Python 3.11
- Flask
- Flask-SQLAlchemy
- google-generativeai==0.2.2

## Setup and Installation

1. Clone the repository:

   ```shell
   https://github.com/sunkarasnigdha/Travel-Itinerary-Generator-Using-AI.git
   cd Travel-Itinerary-Generator-Using-AI
2. Install required packages:

   ```shell
   pip install -r requirements.txt
   ```

## API Keys
- Visual Crossing Weather API Key: [Sign up](https://www.visualcrossing.com/weather-api) for a free account and get your API key.
- Google Palm API: [Sign up](https://makersuite.google.com) for a free account and get your API key.

## Usage
- Please follow the instructions below to run the application locally.

Write API keys: In a `.env` file.
```shell
WEATHER_API_KEY='Your Visual Crossing Weather API Key'
PALM_API_KEY='Your Google Palm API Key'
```
and save it in the root directory of the project.

Run the following command to start the application:
```shell
python wsgi.py
```

## Screenshots

**Home Page of Travel Itinerary Generator without Login.**
![Image](https://github.com/user-attachments/assets/380d2713-c122-4472-99f8-d61ee926e88a)


**Register Page / Sign Up**
![Image](https://github.com/user-attachments/assets/f741cacf-314f-4576-895f-3bf6dbbf4957)


**Login Page**
![Image](https://github.com/user-attachments/assets/5f34f409-e00a-44cc-9a28-fd03a79a9223)


**For Testing, I have taken Source Point as Hyderabad & Destination as Delhi, Starting Date of Journey: 16/05/2025, Return Date: 19/05/2025**
![Image](https://github.com/user-attachments/assets/b9e8dfd4-dfee-4d20-b463-342e3dbf7614)

**Itinerary Page**
![Image](https://github.com/user-attachments/assets/5eb38b9d-2861-4955-9b1e-0aec1e1d20ea)

![Image](https://github.com/user-attachments/assets/5bd6821b-ef59-44e2-9e93-9c6b80c563e3)

**Weather Forecast**
![Image](https://github.com/user-attachments/assets/f38b846c-2951-4c1d-b8d1-2e2ed87184b3)

**Text Translator**
![Image](https://github.com/user-attachments/assets/8cb573ab-cd03-42a1-bd93-0534bd6a116f)



## License

This project is licensed under the [Apache License 2.0](LICENSE) - see the [LICENSE](LICENSE) file for details.
