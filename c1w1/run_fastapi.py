# https://stackoverflow.com/questions/63833593/how-to-run-fastapi-uvicorn-in-google-colab
import nest_asyncio
from pyngrok import ngrok
import uvicorn
import app

ngrok_tunnel = ngrok.connect(8000)
print('Public URL:', ngrok_tunnel.public_url)
nest_asyncio.apply()
uvicorn.run(app, port=8000)