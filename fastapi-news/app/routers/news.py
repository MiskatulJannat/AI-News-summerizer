from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import crud, models, schemas, dependencies, scraper
import logging

router = APIRouter(
    prefix="/news",
    tags=["news"],
)

@router.get("/", response_model=List[schemas.News])
def read_news_list(skip: int = 0, limit: int = 10, db: Session = Depends(dependencies.get_db)):
    news_list = crud.get_news_list(db=db, skip=skip, limit=limit)
    if news_list is None:
        raise HTTPException(status_code=404, detail="News not found")
    return news_list

@router.get("/{news_id}", response_model=schemas.News)
def read_news(news_id: int, db: Session = Depends(dependencies.get_db)):
    news = crud.get_news(db, news_id=news_id)
    if news is None:
        raise HTTPException(status_code=404, detail="News not found")
    return news

@router.post("/scrape/", response_model=List[schemas.News])
def scrape_news(urls: List[str], db: Session = Depends(dependencies.get_db)):
    all_inserted_news = []
    for url in urls:
        inserted_news = scraper.scrape_and_store_news(url, db)
        if inserted_news is None:
            raise HTTPException(status_code=500, detail=f"Error scraping news from {url}")
        all_inserted_news.append(inserted_news)
    return all_inserted_news
