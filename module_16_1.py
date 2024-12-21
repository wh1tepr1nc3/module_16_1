# uvicorn module_16_1:app --reload
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def get_main_page():
    return {"message": "Главная страница"}


@app.get("/user/admin")
async def get_admin_page():
    return {"message": "Вы вошли как администратор"}


@app.get("/user/{user_id}")
async def get_user_number(user_id: str):
    return {"message": f"Вы вошли как пользователь № {user_id}"}


@app.get("/user")
async def get_user_info(username: str, age: int):
    return {'message': f"Информация о пользователе. Имя: {username}, Возраст: {age}"}