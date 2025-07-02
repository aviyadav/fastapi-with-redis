# fastapi-with-redis

### create virtual env (on *nix or win)
- > python -m venv .venv

### acivate the virtual env
- WIN
   > .venv\Scripts\Activate.ps1
- *nix
   > source .venv/bin/activate

### install the libraries
> pip install -r requirements.txt

### run application
> uvicorn main:app --reload

### run redis queue (another window from inside virtual env) `only on *nix or WSL2`
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
