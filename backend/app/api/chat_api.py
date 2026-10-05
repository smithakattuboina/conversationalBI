from fastapi import APIRouter

from backend.app.schemas.chat_schema import ChatRequest
from backend.app.services.chat_service import save_chat
from backend.app.ai.ollama_service import get_ai_response

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


@router.post("/")
def chat(request: ChatRequest):

    # Get response from Llama 3
    ai_response = get_ai_response(request.message)

    # Save into database
    save_chat(request.message, ai_response)

    return {
        "response": ai_response
    }