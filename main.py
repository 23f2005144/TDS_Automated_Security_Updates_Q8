from fastapi import FastAPI
import pandas as pd
import requests
import uvicorn

app = FastAPI(title="Placeholder FastAPI Project")

# Sample endpoint: simple JSON response
@app.get("/")
async def root():
    return {"message": "Hello from FastAPI + pandas + requests!"}

# Sample endpoint: load data with pandas
@app.get("/data")
async def get_data():
    # Example: create a DataFrame
    df = pd.DataFrame({
        "name": ["Alice", "Bob", "Charlie"],
        "age": [25, 30, 35]
    })
    # Return as JSON
    return df.to_dict(orient="records")

# Sample endpoint: fetch data from a public API with requests
@app.get("/joke")
async def get_joke():
    try:
        response = requests.get("https://official-joke-api.appspot.com/jokes/random")
        response.raise_for_status()
        joke = response.json()
        return {"setup": joke.get("setup"), "punchline": joke.get("punchline")}
    except requests.RequestException as e:
        return {"error": str(e)}

# --- Main entry point ---
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5555, reload=True)
