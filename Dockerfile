<<<<<<< HEAD
FROM python:3.10.12

WORKDIR /app

COPY ./app .

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "2113"]
=======
# Stage 1: Build the application
FROM node:20.15.1 AS build
WORKDIR /app
COPY ./package*.json ./
RUN npm install
COPY . .
RUN npm run build

# Stage 2: Serve the application using nginx
FROM nginx:1.18.0
COPY --from=build /app/dist /usr/share/nginx/html/cm-frontend
COPY nginx.conf /etc/nginx/nginx.conf
>>>>>>> f92649972cb7af9171e5fba41d00cbb54f2d313d
