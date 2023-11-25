import requests
import dotenv
import os

dotenv_path = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_path)

def recipe_search(ingredient, meal_type, excluded_item):
    app_id = os.environ.get("APP_ID")
    app_key = os.environ.get("APP_KEY")
    url = 'https://api.edamam.com/api/recipes/v2?type=public&q={}&app_id={}&app_key={}&mealType={}'.format(ingredient, app_id, app_key, meal_type.capitalize())

    if excluded_item:
        url += "&excluded={}".format(excluded_item) # if exlcuded is not empty

    result = requests.get(
        url
    )

    if result.status_code == 200:
        data = result.json()
        if 'hits' in data:
            return data['hits']
        else:
            print("No 'hits' in response")
            return []
    else:
        print("Failed to fetch data")
        return []
    return (result.json()["hits"])

def run():
    ingredient = input('Enter an ingredient: ')
    meal_type = input('Enter a meal type: ')
    excluded_item = input('Enter an ingredient to exclude (press enter to skip): ')
    results = recipe_search(ingredient, meal_type, excluded_item)

    for result in results:
        recipe = result['recipe']

        print(recipe['label'])
        print(recipe['url'])
        print()

run()


