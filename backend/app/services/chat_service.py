from backend.app.database.session import SessionLocal
from backend.app.models.chat import ChatHistory


def save_chat(user_query, ai_response):

    db = SessionLocal()

    chat = ChatHistory(
        user_query=user_query,
        ai_response=ai_response
    )

    db.add(chat)
    db.commit()
    db.refresh(chat)
    db.close()

    return chat