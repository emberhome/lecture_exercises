FROM python:3.8.14

#Do not use env as this would persist after the build and would impact your containers, children images
ARG DEBIAN_FRONTEND=noninteractive

# force the stdout and stderr streams to be unbuffered.
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
  && apt-get -y upgrade \
  && pip install uvicorn fastapi

#Setup workdir
WORKDIR /app

COPY ./  ./

EXPOSE 8000
RUN ls -a

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
