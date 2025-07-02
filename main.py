from fastapi import FastAPI
from redis import Redis
from rq import Queue
from pydantic import BaseModel
from job import print_numbers

app = FastAPI()

class JobData(BaseModel):
    lowest: int
    highest: int


redis_conn = Redis(host='localhost', port=6379)
task_queue = Queue("task_queue", connection=redis_conn)

@app.get("/")
async def read_root():
    return {
        "success": True,
        "message": "pong"
    }

@app.post("/job")
async def post_job(job: JobData):
    lowest = job.lowest
    highest = job.highest

    if lowest > highest:
        return {
            "success": False,
            "message": "Lowest number must be less than or equal to highest number."
        }

    # Enqueue the job to the task queue
    job_instance = task_queue.enqueue(print_numbers, lowest, highest)
    return {
        "success": True,
        "job_id": job_instance.id
    }
