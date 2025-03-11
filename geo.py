# This is a simple game where you guess a country

import random  # This helps us pick a random country

def guess_the_country():
    print("Welcome to Guess the Country!")
    print("I'm thinking of a country. Can you guess it?")

    # Here's a list of 50 countries the game can pick from
    countries = [
        "Canada", "Brazil", "Japan", "Germany", "Australia", "India", "Italy", "Egypt", "Mexico", "Thailand",
        "France", "China", "Russia", "United States", "United Kingdom", "Argentina", "South Africa", "Spain", "Turkey", "South Korea",
        "Indonesia", "Saudi Arabia", "Nigeria", "Pakistan", "Bangladesh", "Vietnam", "Philippines", "Iran", "Ethiopia", "Colombia",
        "Kenya", "Poland", "Ukraine", "Morocco", "Peru", "Malaysia", "Iraq", "Chile", "Netherlands", "Belgium",
        "Sweden", "Greece", "Portugal", "Austria", "Switzerland", "Norway", "Denmark", "Finland", "New Zealand", "Ireland"
    ]

    # The computer picks a random country from the list
    secret_country = random.choice(countries).lower()  # Make it lowercase to make guessing easier
    attempts = 0  # This counts how many guesses the player has made
    max_attempts = 5  # The player gets 5 tries to guess

    # This dictionary gives hints about where each country is located
    continent_hint = {
        "canada": "North America",
        "brazil": "South America",
        "japan": "Asia",
        "germany": "Europe",
        "australia": "The land down under",  # Australia is special :)
        "india": "Asia",
        "italy": "Europe",
        "egypt": "Africa",
        "mexico": "North America",
        "thailand": "Asia",
        "france": "Europe",
        "china": "Asia",
        "russia": "Europe/Asia",  # Russia spans two continents
        "united states": "North America",
        "united kingdom": "Europe",
        "argentina": "South America",
        "south africa": "Africa",
        "spain": "Europe",
        "turkey": "Asia/Europe",  # Turkey spans two continents
        "south korea": "Asia",
        "indonesia": "Asia",
        "saudi arabia": "Asia",
        "nigeria": "Africa",
        "pakistan": "Asia",
        "bangladesh": "Asia",
        "vietnam": "Asia",
        "philippines": "Asia",
        "iran": "Asia",
        "ethiopia": "Africa",
        "colombia": "South America",
        "kenya": "Africa",
        "poland": "Europe",
        "ukraine": "Europe",
        "morocco": "Africa",
        "peru": "South America",
        "malaysia": "Asia",
        "iraq": "Asia",
        "chile": "South America",
        "netherlands": "Europe",
        "belgium": "Europe",
        "sweden": "Europe",
        "greece": "Europe",
        "portugal": "Europe",
        "austria": "Europe",
        "switzerland": "Europe",
        "norway": "Europe",
        "denmark": "Europe",
        "finland": "Europe",
        "new zealand": "Oceania",
        "ireland": "Europe"
    }

    # This dictionary gives unique hints for each country (for attempt 2)
    unique_hints = {
        "canada": "This country is known for its maple syrup and Niagara Falls.",
        "brazil": "This country is home to the Amazon Rainforest and the Carnival festival.",
        "japan": "This country is famous for sushi, anime, and Mount Fuji.",
        "germany": "This country is known for its beer, sausages, and the Brandenburg Gate.",
        "australia": "This country is home to kangaroos and the Sydney Opera House.",
        "india": "This country is known for the Taj Mahal, Bollywood, and spicy food.",
        "italy": "This country is famous for pizza, pasta, and the Colosseum.",
        "egypt": "This country is home to the Pyramids of Giza and the Nile River.",
        "mexico": "This country is known for tacos, Day of the Dead, and Chichen Itza.",
        "thailand": "This country is famous for its beaches, temples, and spicy cuisine.",
        "france": "This country is known for the Eiffel Tower, wine, and the Louvre Museum.",
        "china": "This country is home to the Great Wall and pandas.",
        "russia": "This country is known for its vast size, vodka, and the Kremlin.",
        "united states": "This country is famous for Hollywood, the Statue of Liberty, and fast food.",
        "united kingdom": "This country is known for Big Ben, tea, and the Royal Family.",
        "argentina": "This country is famous for tango, steak, and the Andes Mountains.",
        "south africa": "This country is known for safaris, Nelson Mandela, and Table Mountain.",
        "spain": "This country is famous for flamenco dancing, paella, and La Sagrada Familia.",
        "turkey": "This country is known for kebabs, the Hagia Sophia, and Cappadocia.",
        "south korea": "This country is famous for K-pop, kimchi, and Seoul.",
        "indonesia": "This country is known for Bali, Komodo dragons, and Borobudur Temple.",
        "saudi arabia": "This country is famous for oil, the Arabian Desert, and Mecca.",
        "nigeria": "This country is known for Nollywood, jollof rice, and the Niger River.",
        "pakistan": "This country is famous for the Karakoram Mountains, Lahore Fort, and biryani.",
        "bangladesh": "This country is known for the Sundarbans, tea plantations, and rickshaws.",
        "vietnam": "This country is famous for pho, Ha Long Bay, and the Mekong Delta.",
        "philippines": "This country is known for its beaches, jeepneys, and adobo.",
        "iran": "This country is famous for Persian carpets, the Caspian Sea, and ancient ruins.",
        "ethiopia": "This country is known for coffee, the Simien Mountains, and Lucy (the fossil).",
        "colombia": "This country is famous for coffee, salsa dancing, and the Amazon Rainforest.",
        "kenya": "This country is known for safaris, Mount Kenya, and the Maasai Mara.",
        "poland": "This country is famous for pierogi, Chopin, and the Wieliczka Salt Mine.",
        "ukraine": "This country is known for borscht, Chernobyl, and the Carpathian Mountains.",
        "morocco": "This country is famous for tagine, the Sahara Desert, and Marrakech.",
        "peru": "This country is known for Machu Picchu, llamas, and ceviche.",
        "malaysia": "This country is famous for the Petronas Towers, rainforests, and nasi lemak.",
        "iraq": "This country is known for ancient Mesopotamia, the Tigris River, and Babylon.",
        "chile": "This country is famous for the Atacama Desert, Patagonia, and wine.",
        "netherlands": "This country is known for tulips, windmills, and Amsterdam.",
        "belgium": "This country is famous for waffles, chocolate, and the Atomium.",
        "sweden": "This country is known for IKEA, ABBA, and the Northern Lights.",
        "greece": "This country is famous for the Parthenon, Greek mythology, and feta cheese.",
        "portugal": "This country is known for port wine, Lisbon, and the Algarve.",
        "austria": "This country is famous for Mozart, Vienna, and the Alps.",
        "switzerland": "This country is known for chocolate, watches, and the Swiss Alps.",
        "norway": "This country is famous for fjords, Vikings, and the Northern Lights.",
        "denmark": "This country is known for LEGO, Hans Christian Andersen, and Copenhagen.",
        "finland": "This country is famous for saunas, Santa Claus, and Nokia.",
        "new zealand": "This country is known for hobbits, rugby, and stunning landscapes.",
        "ireland": "This country is famous for Guinness, leprechauns, and the Cliffs of Moher."
    }

    # Give the player a hint about the continent
    print(f"Hint: The country is in {continent_hint[secret_country]}.")

    # Let the player guess up to 5 times
    while attempts < max_attempts:
        guess = input("\nEnter your guess: ").lower()  # Get the player's guess and make it lowercase
        attempts += 1  # Add 1 to the number of attempts

        if guess == secret_country:  # Check if the guess is correct
            print(f"Congratulations! You guessed the country in {attempts} attempts!")
            break  # End the game if the guess is correct
        else:
            print("Incorrect! Try again.")  # Tell the player they're wrong

            # Give more hints after certain attempts
            if attempts == 2:
                print(f"Hint: {unique_hints[secret_country]}")  # Unique hint for attempt 2
            elif attempts == 4:
                print(f"Hint: The country has {len(secret_country)} letters.")

    # If the player runs out of attempts, tell them the answer
    if attempts >= max_attempts:
        print(f"\nSorry, you've run out of attempts. The country was {secret_country.capitalize()}.")

    print("Thanks for playing!")  # Say goodbye

# This runs the game when you start the program
if __name__ == "__main__":
    guess_the_country()