# fastapi-with-redis

### run application
> uvicorn main:app --reload

### run redis queue (from inside virtual env)
> rq worker task_queue

## API 
### API docs [SWAGGER]
> localhost:8000/docs

### Run the API to post the messages in Redis
> POST - localhost:8000/job

<code>
BODY
{
    "lowest": 5,
    "highest": 25
}
</code>


### response:

<code>
{
    "success": true,
    "job_id": "3d640fdd-891f-46aa-bffa-0e69f1946b7d"
}
</code>

<img title="job" alt="enque-job" src="/job.png">
