from fastapi import FastAPI,HTTPException

app = FastAPI()

code = 500

if code != 200:
    with open('artifact.txt','w') as f:
        f.write(f'error code {code}')

@app.get('/')
def read_root():
    return {'hello' : 'world'}

@app.get('/book/{book_id}')
def read_book(book_id: int):
    if book_id > 10:
        raise HTTPException(status_code=404,
                            detail='Book not found')
    return {'book_id': book_id}