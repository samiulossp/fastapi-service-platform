from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from sqlalchemy import text

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "FastAPI service platform is running!"}

@app.get('/test-db')
async def test_db(db : Session = Depends(get_db)):
    try:
        result = db.execute(text("SELECT 1"))
        result.fetchone()
        return {"message": "Database is Connected!"}
    except Exception as e:
        return {"error": str(e)}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8889, reload=False)