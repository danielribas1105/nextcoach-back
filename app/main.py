from fastapi import FastAPI
from app.routers import auth, usuarios, workout_plans

app = FastAPI(
    title="NextCoachAI API",
    description="API para gerenciamento de planos de treino",
    version="0.0.1",
)

# Registra todos os routers
app.include_router(auth.router)
app.include_router(usuarios.router)
app.include_router(workout_plans.router)


@app.get("/", tags=["Health"])
def health_check():
    return {"status": "ok"}
