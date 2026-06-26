# End-to-End MLOps Pipeline

## Student Information

**Name:** Manish Kumar
**Roll Number:** G25AI1068

## Repository Branches

* main – Initial repository setup
* dev – Model development and CI/CD workflow
* docker_cicd – Flask application, Docker configuration, and deployment files

## Project Overview

This project implements an end-to-end MLOps pipeline using the Olivetti Faces dataset from scikit-learn.

The project includes:

* Model training using DecisionTreeClassifier
* Model testing and evaluation
* Git branching strategy
* GitHub Actions CI/CD workflow
* Flask web application
* Docker containerization setup
* Kubernetes deployment configuration

## Dataset

Dataset used: Olivetti Faces Dataset

Source:

```python
from sklearn.datasets import fetch_olivetti_faces
```

## Model

Algorithm:

* DecisionTreeClassifier

Train/Test Split:

* Training Data: 70%
* Testing Data: 30%

Model file:

```text
savedmodel.pth
```

## Project Structure

```text
MLops-Assignment/
│
├── train.py
├── test.py
├── app.py
├── Dockerfile
├── requirements.txt
├── savedmodel.pth
├── README.md
├── .gitignore
│
└── .github/
    └── workflows/
        └── ci.yml
```

## CI/CD Workflow

GitHub Actions workflow automatically:

1. Checks out repository
2. Installs dependencies
3. Runs train.py
4. Runs test.py
5. Validates repository functionality

Workflow file:

```text
.github/workflows/ci.yml
```

## Flask Application

The Flask application serves the machine learning model and provides a web interface for prediction.

Run locally:

```bash
python app.py
```

Application URL:

```text
http://localhost:5000
```

## Docker

Build Docker image:

```bash
docker build -t mlops-app .
```

Run Docker container:

```bash
docker run -p 5000:5000 mlops-app
```

## Author

Manish Kumar
Roll No: G25AI1068

## Current Status

Completed:
- Git Repository Setup
- Branch Management (main, dev, docker_cicd)
- Model Training (DecisionTreeClassifier)
- Model Testing
- GitHub Actions CI/CD Workflow
- Flask Application
- Dockerfile
- Requirements File

Pending due to virtualization issue:
- Docker Image Build
- Docker Hub Push
- Kubernetes Deployment
## Challenges Faced

During Docker setup, Docker Desktop could not start because virtualization support was not available on the system.

Observed error:

```text
Virtualization support not detected
Docker Desktop failed to start because virtualisation support wasn’t detected

