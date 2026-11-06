from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def check_helath():
    return {
        "status": "OK"
    }

@app.post("/ask-questoin")
def ask_question():
    pass