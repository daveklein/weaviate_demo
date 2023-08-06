# Pizza Recommendation Service with Weaviate Vector Database

Load a db with randomly created pizzas in JSON format, then pass a sample pizza to the recommendation service to find similar pizzas using a Weaviate query.

## Getting Started

Ro run this project you will need an account with Weaviate, which you can get for free at [https://weaviate.io](https://weaviate.io).  You will also need a Hugging Face account: [https://huggingface.co/](https://huggingface.co/).  

Use the endpoint and api key from Weaviate, as well as the Hugging Face token to fill in the values in `config.py`. 

Then, run `pizza_loader.py` to load your vector db with random pizzas. You may run it multiple times to load more pizzas, but you should comment out the schema creation statement at line 28, as it only needs to be executed once.

Now you can run `recommendation_service.py`, which is a Flask microservice. 
`python -m flask --app recommendation_service run`

Finally, POST a sample pizza in JSON format and you should get three suggestions back, aloong with their certainty scores. 

