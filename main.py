from fastapi import FastAPI
from shared.services.gpkg_parser import load_seasonal_ranges
import json, os

app = FastAPI(title="Bird Mapping API")

@app.get("/api/species/{species_code}/{season}")
def get_season_data(species_code: str, season: str):
    path = f"data/{species_code}_range_smooth_27km_2023.gpkg"
    if not os.path.exists(path):
        return {"error": "file not found"}
    ranges = load_seasonal_ranges(path)
    if season not in ranges:
        return {"error": "season not found"}
    return json.loads(ranges[season].to_json())
