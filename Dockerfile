FROM python:3.10-slim

ENV APP_HOME /app
WORKDIR $APP_HOME

RUN apt-get update && apt-get install -y --no-install-recommends \
	chromium \
	chromium-driver \
	&& rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . ./

ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER=/usr/bin/chromedriver

EXPOSE 8081

CMD ["python", "main.py"]
