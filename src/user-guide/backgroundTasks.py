import time
from fastapi import FastAPI, BackgroundTasks, status
from pydantic import BaseModel


app = FastAPI()

def write_notification(email: str, message = ""):
    with open('log.txt', mode='w') as email_file:
        content = f"notication  for {email}: {message}"
        time.sleep(5)
        email_file.write(content)


@app.post("/send-notification/{email}", status_code=status.HTTP_202_ACCEPTED)
async def send_notification(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_notification, email, message="some notification")
    return {"message": "Notification sent in the background"}

