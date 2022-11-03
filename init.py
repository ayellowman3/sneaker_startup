import os
os.system("pip install requests")
os.system("pip install fastapi")
os.system("pip install uvicorn")
from startup import pull_sneakers
pull_sneakers.main()


#cd Documents\Coding\sneakers_startup
os.system("cd backend")
os.system(f"docker build . -t customerapi -f Dockerfile")
os.system("cd ..")
os.system("cd frontend")
os.system(f"docker build . -t clientapi -f Dockerfile")
os.system("cd ..")
#os.system("docker run -p 8000:8000 customerapi")
#os.system("docker run -p 8000:8000 customerapi")
#os.system("docker run -p 9000:9000 clientapi")
os.system("docker-compose up --build")
