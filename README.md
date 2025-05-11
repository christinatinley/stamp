## stamp

stamp is an AI-powered itinerary travel assistant tool- aiming to ease the travel planning process into one seamless experience. Users take a short quiz to let stamp know what their preferences are including, but not limited to, location, dates, cuisine preferences, level of interests in different activities, etc. Once 
the quiz has been completed, stamp provides an itinerary for the desired trip. 

## Architecture and Tools
This application's frontend was built using Vue.js, alongside Primvue for UI components. (insert info about backend and model being used here)

## Setup
To get this project up and running locally: 
1. Clone the repository
2. Install dependencies:
   - run `npm install` in the client folder
   - run `pip install -r requirements.txt` in the server folder
3. Create a .env file
   - Obtain an API key for the Google Places API and call it `PLACES_API_KEY`
   - Obtain an API key for the Mistral API and call it `MISTRAL_API_KEY`
5. Run the development server:
   - run `npm run dev` to run the frontend
   - run `flask run` to run the backend

## Component Libraries
Within this vue application, we are using Primevue as our UI component library. (https://primevue.org/) 
