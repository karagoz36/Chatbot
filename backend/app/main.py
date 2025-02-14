from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.services.scaleway_service import ScalewayService

app = FastAPI()

# CORS ayarları
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080", "http://localhost:3000"],  # İzin verilen originler
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)

class PromptRequest(BaseModel):
    prompt: str

scaleway_service = ScalewayService()

@app.post("/api/generate")
async def generate_text(prompt_request: PromptRequest):
    try:
        print(f"Received prompt: {prompt_request.prompt}")
        response = await scaleway_service.generate_text(prompt_request.prompt)
        return {"content": response}
    except Exception as e:
        print(f"Error: {str(e)}")
        return {"error": str(e)}

@app.get("/")
async def root():
    return {"message": "AI API is running"}
