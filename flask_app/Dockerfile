FROM python:3.11.3

RUN mkdir -p /usr/src/koneurakointi
WORKDIR /usr/src/koneurakointi
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . /usr/src/koneurakointi

EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
