# 🚀 Emoji Predictor Deployment (FastAPI + Docker + AWS)

## 🎥 Demo Video
[Watch Demo Video](https://drive.google.com/file/d/1Vba68zBCBfDI7oazhP9TWkYiixRs4zqM/view?usp=sharing)

## 📌 Overview
This project deploys an LSTM-based emoji prediction model using FastAPI, Docker, and AWS EC2 with Nginx.

## ⚙️ Tech Stack
- FastAPI
- Docker
- AWS EC2
- Nginx
- TensorFlow/Keras

## 🚀 Features
- REST API for emoji prediction
- Dockerized application
- Live deployment on AWS

## ▶️ Run Locally
```bash
pip install -r requirements.txt
uvicorn app:app --reload

# 🚀 Emoji Predictor Deployment (FastAPI + Docker + AWS)

## 📌 Overview
This project deploys an LSTM-based emoji prediction model using FastAPI, Docker, and AWS EC2 with Nginx.

## ⚙️ Tech Stack
- FastAPI
- Docker
- AWS EC2
- Nginx
- TensorFlow/Keras

## 🚀 Features
- REST API for emoji prediction
- Dockerized application
- Live deployment on AWS

## ▶️ Run Locally
```bash
pip install -r requirements.txt
uvicorn app:app --reload

docker build -t emoji-api .
docker run -p 8000:8000 emoji-api

