import fastapi
import uvicorn


app = fastapi.FastAPI()


@app.get('/')
def index():
    context = fastapi.responses.PlainTextResponse('Hello')
    
    return context

if __name__ == "__main__":
    uvicorn.run(app)