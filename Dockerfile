# -------- Frontend Build Stage --------
FROM node:20 AS frontend-builder

WORKDIR /app/frontend
COPY frontend/ ./
RUN npm install
RUN npm run build

# -------- Backend Stage --------
FROM python:3.10-slim AS backend

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/ ./backend
COPY data/ ./data
COPY .env .env

CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]

# -------- Final Stage (Nginx + Static Frontend) --------
FROM nginx:alpine
COPY --from=frontend-builder /app/frontend/dist /usr/share/nginx/html
COPY --from=backend /app /app
EXPOSE 80
