FROM informaticsmatters/rdkit-python3-debian:Release_2020_03

USER root
# ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update

RUN apt-get install libpango1.0-0 -y
RUN apt-get install libcairo2 -y
RUN apt-get install libpq-dev -y


COPY requirements.txt .
RUN pip3 install -r requirements.txt

WORKDIR /app
COPY templates ./templates
COPY static ./static
COPY web-app.py ./

# For webapp

# Define our command to be run when launching the container
CMD gunicorn web-app:app --bind 0.0.0.0:$PORT --reload

# EXPOSE 8080
# ENTRYPOINT ["python3", "web-app.py"]
# EXPOSE 5000