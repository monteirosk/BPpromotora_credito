from fastapi import FastAPI
from my_scrapy import get_years, get_all, get_data
from typing import List, Optional
from fastapi.responses import Response
import pandas as pd
import json

app = FastAPI(title="Teste Técnico - Desenvolvedor Pleno RPA", docs_url="/", openapi_url="/openapi.json")

@app.get("/years", summary="Lista os anos que tem dados disponíveis no site", response_model=List[str])
async def get_years_handler():
    return get_years()

@app.get("/all", summary="Exporta todos os dados disponíveis no site no formato JSON",response_class=Response)
async def get_all_json_file_handler():
    df = get_all()
    df = df.to_json(orient='records')
    
    headers = { "Content-Disposition": 'attachment; filename="dados_completos.json"'}
    response = Response(content=df, media_type="application/json", headers=headers)
    return response


@app.get("/data/{year}", summary="Exporta os dados de um ano específico no formato JSON",response_class=Response)
async def get_by_year_handler(year:int):
    data = get_data(year)
    json_data = json.dumps(data, ensure_ascii=False).encode('utf8')
    headers = {"Content-Disposition": f'attachment; filename="dados_{year}.json"'}
    response = Response(content=json_data, media_type="application/json", headers=headers)
    return response



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)