FROM python:3.6.9

WORKDIR usr/src/koneurakointi
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
COPY . .

CMD ["gunicorn", "--workers:2", "--bind", "0.0.0.0:5000", "wsgi:app"]
