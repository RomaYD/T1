# generated by fastapi-codegen:
#   filename:  sprints.yaml
#   timestamp: 2024-11-16T00:19:36+00:00

from __future__ import annotations

from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware

from models import SprintsListFilter

app = FastAPI(
    title='Swagger Sprint - OpenAPI 3.0',
    description='This is a Sprints Server ',
    version='1.0.11',
    servers=[{'url': 'https://sprints.swagger.io/api/v3'}],
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

@app.post('/sprints/list', response_model=None)
def post_sprints_list(body: SprintsListFilter) -> None:
    pass


@app.post('/sprints/metric', response_model=None)
def post_sprints_metric(body: SprintsListFilter) -> None:
    pass


@app.post('/sprints/upload', response_model=None)
def post_sprints_upload(file: list[UploadFile]) -> None:
    print("lpl")
    files_decoded = []
    for curr_file in file:
        file_content = curr_file.file.read()  # Читаем закодированные данные
        try:
            file_content_nonbytes = file_content.decode('utf-8')  # Декодируем Base64
            files_decoded.append(file_content_nonbytes)
        except Exception as e:
            print({"filename": curr_file.filename, "error": str(e)})  # Обработка ошибок декодирования

    print(files_decoded)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
