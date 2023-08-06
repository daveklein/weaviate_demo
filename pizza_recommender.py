import weaviate
import json
from config import wv, hf

client = weaviate.Client(
    url = wv["endpoint"],  
    auth_client_secret=weaviate.AuthApiKey(api_key=wv["api_key"]),
    additional_headers = {
        "X-HuggingFace-Api-Key": hf["token"]
    }
)

def suggest_pizzas(sample):
    
    nearText = {"concepts": [sample]}
    response = (
        client.query
        .get("Pizza", ["cheese", "meats", "veggies"])
        .with_near_text(nearText)
        .with_limit(3)
        .with_additional(['certainty'])
        .do()
    )
    return json.dumps(response, indent=4)
