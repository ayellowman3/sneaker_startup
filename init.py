import os
os.system("pip install requests")
os.system("pip install fastapi")
os.system("pip install uvicorn")
from startup import pull_sneakers
pull_sneakers.main()


#cd Documents\Coding\sneakers_startup
os.system("docker build -t customerapi")
os.system("docker run -p 8000:8000 customerapi")
