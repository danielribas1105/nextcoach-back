from fastapi import FastAPI

# Importa todos os models para o SQLAlchemy registrar
from app.modules.user.model import User
from app.modules.user_session.model import UserSession
from app.modules.account.model import Account
from app.modules.workout_plan.model import WorkoutPlan
from app.modules.workout_day.model import WorkoutDay
from app.modules.workout_exercise.model import WorkoutExercise
from app.modules.workout_session.model import WorkoutSession

from app.modules.user.route import router as user_router
from app.modules.workout_plan.route import router as workout_plan_router
from app.modules.workout_day.route import router as workout_day_router
from app.modules.workout_exercise.route import router as workout_exercise_router
from app.modules.workout_session.route import router as workout_session_router

app = FastAPI(
    title="NextCoachAI API",
    description="API para gerenciamento de planos de treino",
    version="1.0.0"
)

app.include_router(user_router)
app.include_router(workout_plan_router)
app.include_router(workout_day_router)
app.include_router(workout_exercise_router)
app.include_router(workout_session_router)

@app.get("/", tags=["Health"])
def health_check():
    return {"status": "ok"}