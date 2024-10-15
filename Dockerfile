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
