import fastapi
import uvicorn


app = fastapi.FastAPI()


@app.get('/')
def index():
    {
        'message': "Loading..."
    }
    
    
if __name__ == "__main__":
    uvicorn.run(app)