# import time
from fastapi import FastAPI, BackgroundTasks, status, Depends
from typing import Annotated


app = FastAPI()

# def write_notification(email: str, message = ""):
#     with open('log.txt', mode='w') as email_file:
#         content = f"notication  for {email}: {message}"
#         time.sleep(5)
#         email_file.write(content)


# @app.post("/send-notification/{email}", status_code=status.HTTP_202_ACCEPTED)
# async def send_notification(email: str, background_tasks: BackgroundTasks):
#     background_tasks.add_task(write_notification, email, message="some notification")
#     return {"message": "Notification sent in the background"}

# 'a' - writes it to the end
def write_log(message: str):
    with open('log.txt', mode='a') as log:
        log.write(message)

def get_query(background_tasks: BackgroundTasks, q: str | None = None):
    if q:
        message = f"found query: {q}\n"
        background_tasks.add_task(write_log, message)
    return q


@app.post("/send-notification/email", status_code=status.HTTP_202_ACCEPTED)
async def send_notification(
    email: str, background_task: BackgroundTasks, q: Annotated[str, Depends(get_query)]
):
    message = f"message to {email}"
    background_task.add_task(write_log, message)
    return {"message": "Message sent focker", "query": q}