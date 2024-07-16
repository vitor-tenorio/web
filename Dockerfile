FROM python:3.11.5-alpine3.17
COPY ./horse_farm_management /horse_farm_management
WORKDIR /horse_farm_management
RUN pip install --no-cache-dir -r Requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
