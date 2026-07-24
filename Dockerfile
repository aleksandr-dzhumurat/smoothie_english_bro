FROM python:3.12

ENV PYTHONPATH=/srv \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /srv/

RUN apt-get update \
    && apt-get install -y --no-install-recommends ffmpeg \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /srv/
RUN python3.12 -m pip install --no-cache-dir -r requirements.txt

COPY . /srv/

CMD ["python3.12", "src/app.py"]
