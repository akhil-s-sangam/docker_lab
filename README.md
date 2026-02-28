# 📦 Dockerized Machine Learning Lab

## Wine Classification using Gradient Boosting

---

## 📌 Assignment Overview

This lab demonstrates how to:

* Modify an existing ML lab
* Use a different dataset and model
* Containerize the ML workflow using Docker
* Build and run the project entirely inside a Docker container

The goal was to ensure the lab is **not identical to the original repository** and includes meaningful modifications aligned with grading requirements.

---

## 🔄 Modifications Made (Compared to Original Lab)

| Original Lab           | Modified Version (This Submission) |
| ---------------------- | ---------------------------------- |
| Iris Dataset           | Wine Dataset                       |
| RandomForestClassifier | GradientBoostingClassifier         |
| No metrics saved       | Accuracy printed                   |
| Basic Dockerfile       | Improved structured Dockerfile     |
| No artifact emphasis   | Model saved as `.pkl`              |

These changes ensure:

* Different dataset
* Different model
* Different output artifact
* Clear demonstration of Docker usage

---

## 📊 Dataset Used

We used the **Wine dataset** from:

scikit-learn

The dataset contains:

* 178 samples
* 13 numerical features
* 3 target classes (wine types)

This dataset is built into sklearn and does not require external downloads.

---

## 🤖 Model Used

Instead of Random Forest, this lab uses:

**GradientBoostingClassifier**

Why this model?

* Ensemble learning method
* Strong performance on structured/tabular data
* More advanced boosting approach compared to bagging

---

## 🐳 Docker Implementation

Everything runs inside a Docker container.

Base image used:

```
python:3.10-slim
```

### Dockerfile Summary

* Sets working directory
* Copies requirements
* Installs dependencies
* Copies source code
* Runs training script

---

## 📁 Project Structure

```
docker_lab/
│
├── Dockerfile
└── src/
    ├── main.py
    └── requirements.txt
```

---

## 🚀 How to Run the Project

### 1️⃣ Build Docker Image

```bash
docker build -t docker_lab:v2 .
```

---

### 2️⃣ Run the Container

```bash
docker run --name ml-container docker_lab:v2
```

---

### Expected Output

```
Model trained successfully!
Accuracy: 0.964
```

---

## 🎯 Learning Outcomes

Through this lab, the following concepts were demonstrated:

* Difference between Docker image and container
* Building custom Docker images
* Running ML training inside container
* Managing dependencies with requirements.txt
* Saving trained models
* Versioning Docker images
* Pushing project to GitHub

---

## 🧠 Concepts Applied

### Containers vs Images

* **Image** → Blueprint (docker_lab:v2)
* **Container** → Running instance of that image

Multiple containers can be created from the same image.

---

## 📌 Why Docker for ML?

Docker ensures:

* Environment consistency
* Reproducibility
* Portability across systems
* Easy deployment
* Clean dependency isolation

This makes ML workflows production-ready.

---

## 📎 GitHub Submission

This repository contains:

* Modified ML code
* Dockerfile
* Requirements file
* Project structure
* Working Docker build

Repository link:

```
https://github.com/akhil-s-sangam/docker_lab
```

---

## ✅ Conclusion

This lab successfully:

* Modified the original assignment
* Used a different dataset and model
* Containerized the ML workflow
* Built and executed everything using Docker
* Pushed final project to GitHub

The project demonstrates understanding of:

* Machine Learning workflow
* Docker fundamentals
* Reproducible environments
* Version control using Git
