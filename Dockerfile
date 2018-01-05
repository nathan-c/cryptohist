FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
# docker run -it --name cryptohist -v "$PWD"/cache:/usr/src/app/cache cryptohist
CMD [ "python", "./run.py" ]