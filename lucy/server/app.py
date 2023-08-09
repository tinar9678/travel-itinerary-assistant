import os
import openai
import json
from flask import Flask, request
from flask_cors import CORS
from dotenv import load_dotenv

app = Flask(__name__)
CORS(app)
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        print(request.get_json())
        [location, duration] = request.get_json()["message"].split("*")
        print(duration)
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(location, duration),
            temperature=0.6,
            max_tokens=200,
        )
        return json.dumps({'data': response.choices[0].text})

    return "hello world"


def generate_prompt(location, duration):
    return """Suggest a detailed itinerary plan for a given destination and duration. 
        The itinerary should include dinner options for each day and 3-4 activities.
        Location: Copenhagen 
        Duration: 2 days
        Itinerary: 
            Day 1: Immerse in Historic Charm
            Morning:

            Breakfast: Start your day with a hearty Scandinavian breakfast at Café Norden, offering a mix of pastries, yogurt, fruits, and Danish open-faced sandwiches.
            Activity: Begin your exploration at the iconic Nyhavn Harbor. Take a leisurely stroll along the colorful quayside, capture photos of the historic houses, and maybe consider taking a canal boat tour for an overview of the city.
            Afternoon:

            Lunch: Enjoy a traditional smørrebrød lunch at Aamanns, a renowned spot for Danish open sandwiches.
            Activity: Visit the Rosenborg Castle, a beautifully preserved Renaissance castle. Explore the royal rooms, admire the Crown Jewels, and stroll through the stunning Rosenborg Castle Gardens.
            Activity: Spend some time at the King's Garden, a serene green space perfect for a relaxing walk or a picnic.
            Evening:

            Dinner: Head to Höst for a contemporary Danish dining experience, featuring modern Nordic cuisine with a focus on seasonal ingredients.
            Activity: Explore Tivoli Gardens, a historic amusement park that offers a mix of rides, beautiful gardens, and evening entertainment.
            Day 2: Modern Vibes and Cultural Immersion

            Morning:

            Breakfast: Enjoy a Scandinavian breakfast buffet at Grød, known for its delicious porridge and innovative toppings.
            Activity: Visit the Round Tower (Rundetårn) for panoramic views of the city. Ascend the unique spiral ramp to the top and take in the breathtaking sights.
            Activity: Explore the Freetown Christiania, an alternative, self-governing neighborhood known for its unique atmosphere, street art, and vibrant culture.
            Afternoon:

            Lunch: Have a quick and delicious street food lunch at Copenhagen Street Food on Paper Island.
            Activity: Discover the National Museum of Denmark, where you can delve into the history and culture of Denmark through a wide range of artifacts and exhibits.
            Activity: Walk along Strøget, one of Europe's longest pedestrian streets, and enjoy shopping for Danish design, fashion, and souvenirs.
            Evening:

            Dinner: Experience a Nordic-inspired seafood dinner at Fiskebaren, offering a selection of fresh and creatively prepared seafood dishes.
            Activity: Conclude your trip with a relaxing sunset visit to the Little Mermaid statue, an iconic symbol of Copenhagen located by the waterfront.
        Location: South Korea 
        Duration: 1 day
        Itinerary: 
        Location: {}
        Duration: {}
        Itinerary:""".format(
                location.capitalize(), duration.capitalize()
        )