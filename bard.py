import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load the environment variables
load_dotenv()
palm_api_key = os.environ.get("PALM_API_KEY")


# Create a config.
genai.configure(api_key=palm_api_key)
model = genai.GenerativeModel(model_name="gemini-1.5-flash")
# print(list(palm.list_models()))


# Generate some text.
def generate_itinerary(source, destination, start_date, end_date, no_of_day):
    prompt = f"Generate a personalized trip itinerary for a {no_of_day}-day trip from {source} to {destination} on {start_date} to {end_date}, with an optimum budget (Currency:INR)."
    response = model.generate_content(prompt)
    return(response.text)