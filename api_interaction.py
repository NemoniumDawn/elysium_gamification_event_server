import requests

NOTION_KEY = "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"
NOTION_DB_ID = "11ee232c7c8181b6a33dd9aba2bfea3e"


# Define the base URL for the PokeAPI
base_url = "https://pokeapi.co/api/v2/pokemon/"


def get_first_pokemon():
    # The ID for the first Pokémon is 1 (Bulbasaur)
    response = requests.get(f"{base_url}1/")

    if response.status_code == 200:
        # Parse the JSON response
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to retrieve data: {response.status_code}")


def add_to_notion(pokemon):
    notion_url = "https://api.notion.com/v1/pages"
    headers = {
        "Authorization": f"Bearer {NOTION_KEY}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28",  # Use the latest version
    }

    # Construct the payload for adding a new page to your Notion DB
    payload = {
        "parent": {"database_id": NOTION_DB_ID},  # Ensure this is correct
        "properties": {
            "Name": {"title": [{"text": {"content": pokemon["name"]}}]},
            "Height": {"number": pokemon["height"]},
            "Weight": {"number": pokemon["weight"]},
        },
    }

    # Send the POST request to create a new page in Notion
    response = requests.post(notion_url, headers=headers, json=payload)

    if response.status_code == 200:
        print("Page created successfully in Notion.")
    else:
        print(
            f"Failed to create page in Notion: {response.status_code} - {response.text}"
        )


# Call the function and print the result
first_pokemon = get_first_pokemon()
if first_pokemon:
    print(f"Name: {first_pokemon['name']}")
    print(f"Height: {first_pokemon['height']}")
    print(f"Weight: {first_pokemon['weight']}")

    # Add Pokémon data to Notion
    add_to_notion(first_pokemon)
