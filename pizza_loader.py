import weaviate
import json
from pizzas import random_pizzas
from config import wv, hf

client = weaviate.Client(
    url = wv["endpoint"],  
    auth_client_secret=weaviate.AuthApiKey(api_key=wv["api_key"]),
    additional_headers = {
        "X-HuggingFace-Api-Key": hf["token"]
    }
)


class_obj = {
    "class": "Pizza",
    "vectorizer": "text2vec-huggingface",  
    "moduleConfig": {
        "text2vec-huggingface": {
            "model": "sentence-transformers/all-MiniLM-L6-v2",  
            "options": {
                "waitForModel": True
            }
        }
    }
}

client.schema.create_class(class_obj)

pizzas = json.loads(random_pizzas(500))

with client.batch(
    batch_size=500
) as batch:
    # Batch import all Pizzas
    for i, pz in enumerate(pizzas):
        print(f"importing pizza: {i+1}")

        properties = {
            "cheese": pz["cheese"],
            "meats": pz["meats"],
            "veggies": pz["veggies"],
        }

        client.batch.add_data_object(
            properties,
            "Pizza",
        )



