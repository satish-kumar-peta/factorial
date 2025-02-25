from fastapi import FastAPI
app=FastAPI()
@app.get("/factorial")
def factorial(n:int):
    fact=1
    for i in  range(1,n+1,+1):
        fact=fact*i
    return fact