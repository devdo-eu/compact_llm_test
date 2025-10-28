from pydantic import BaseModel, Field

class QuestionAnswer(BaseModel):
    question: str = Field(..., description='Pytanie z tekstu')
    answer: str = Field(..., description='Odpowiedź z tekstu na pytanie z tekstu')
    answer_format: str = Field(..., description='Krótki opis spodziewanego formatu odpowiedzi, np. tylko rok w formacie "XXXX roku"')

class ManyQA(BaseModel):
    qa: list[QuestionAnswer] = Field(..., description='Pytania i odpowiedzi z tekstu')