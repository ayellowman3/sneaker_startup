import os
os.system("pip install requests")
os.system("pip install fastapi")
os.system("pip install uvicorn")
from startup import pull_sneakers
pull_sneakers.main()


#cd Documents\Coding\sneakers_startup
os.system(f"docker build . -t customerapi -f backend/Dockerfile")
os.system(f"docker build . -t clientapi -f frontend/Dockerfile")
#os.system("docker run -p 8000:8000 customerapi")
os.system("docker run customerapi")
os.system("docker run clientapi")
