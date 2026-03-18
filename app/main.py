from fastapi import FastAPI
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