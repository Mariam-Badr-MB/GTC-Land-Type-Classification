# 🌍 GTC-Land-Type-Classification
## Project 14: Land Type Classification using Sentinel-2 Satellite Images

![Python](https://img.shields.io/badge/Python-3.10-blue?style=flat-square)
![PyTorch](https://img.shields.io/badge/PyTorch-2.1-red?style=flat-square)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28-orange?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

---

## 🔍 Project Overview
This project develops a machine learning model to classify land cover types in **Egypt** using **Sentinel-2 satellite imagery**.  
The system can detect categories such as:

- 🌾 Agriculture  
- 💧 Water bodies  
- 🏙️ Urban areas  
- 🏜️ Deserts  
- 🛣️ Roads  
- 🌳 Trees

The workflow includes **data preparation**, **exploratory analysis**, **model training & validation**, and **deployment** via a lightweight **web app**.  
Final deliverables include a **trained model**, **performance report**, and an **interactive application** for testing land classification.

---

## 👥 Collaborators & Responsibilities
| Task | Collaborator |
|------|-------------|
| Data Pipeline, EDA & Feature Engineering | Roaa Raafat |
| Model Architecture & Evaluation | Mariam Mohamed |
| Deployment & Dashboard | Mariam Badr |
| Video & GitHub README | Eman Elnaggar & Mariam Elnemrawy |
| Presentation | Mariam Ahmed |

---

## 📦 Dataset
[EuroSAT Dataset (Kaggle)](https://www.kaggle.com/datasets/apollo2506/eurosat-dataset)

---

## 🛠️ Workflow

### 1️⃣ Data Pipeline
- Notebook: `GTC_01_data_pipeline.ipynb`  
- Script: `src/data_pipeline.py`  
- Tasks:
  - Downloads & organizes the EuroSAT dataset  
  - Cleans CSVs and ensures consistent labels  
  - Generates dataset statistics & class maps  
  - Outputs train/validation/test splits  

### 2️⃣ Exploratory Data Analysis
- Notebook: `GTC_02_eda_visualization.ipynb`  
- Tasks:
  - Class distribution plots  
  - Sample images per class (grid view)  
  - Checks for corrupted/missing/duplicate images  
  - RGB intensity histograms  
  - Data augmentation visualizations  
  - Class-level mean RGB statistics  
  - Feature extraction (color histograms, texture descriptors)  

### 3️⃣ Feature Engineering
- Script: `src/features.py`  
- Tasks:
  - Geospatial-safe augmentations (rotation, flip, jitter, crop/zoom)  
  - Normalization & preprocessing utilities  

---

## 📤 Outputs Generated
- `train.csv`, `validation.csv`, `test.csv` (cleaned datasets)  
- `dataset_statistics.json` & plots (`dataset_statistics.png`, `sample_images.png`)  
- `augmentation_examples.png`  
- Engineered features in `data/features/`

---

## ⚡ Quick Start (Colab)
```bash

### 1- Clone the repository
!git clone https://github.com/Mariam-Badr-MB/GTC-Land-Type-Classification.git
%cd GTC-Land-Type-Classification

### 2- Install dependencies
!pip install -r requirements.txt

### 3- Configure Kaggle API
from google.colab import files
uploaded = files.upload()  # upload kaggle.json

!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json

```

### 4- Run Notebooks
 - GTC_01_data_pipeline.ipynb
 - GTC_02_eda_visualization.ipynb

--- 

###  View Presentation
[🎨 Project Presentation on Canva](https://www.canva.com/design/DAG0Dh60JoA/yx_ZVqEv5-SEXtxBMFXqUg/edit?utm_content=DAG0Dh60JoA&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

---


## 📬 Contact
- **Mariam Badr Yehia**: 
  <a href="https://github.com/Mariam-Badr-MB" target="_blank">
    <img src="https://cdn.jsdelivr.net/npm/simple-icons@v9/icons/github.svg" alt="GitHub" width="20"/>
  </a>
  <a href="https://www.linkedin.com/in/mariambadr13/" target="_blank">
    <img src="https://cdn.jsdelivr.net/npm/simple-icons@v9/icons/linkedin.svg" alt="LinkedIn" width="20"/>
  </a>

- **Mariam Mohamed Sayed Mohamed**: 
  <a href="https://github.com/mariam-29" target="_blank">
    <img src="https://cdn.jsdelivr.net/npm/simple-icons@v9/icons/github.svg" alt="GitHub" width="20"/>
  </a>
  <a href="https://www.linkedin.com/in/mariam-elsherif-a61098353/" target="_blank">
    <img src="https://cdn.jsdelivr.net/npm/simple-icons@v9/icons/linkedin.svg" alt="LinkedIn" width="20"/>
  </a>

- **Mariam Mohamed Elnemrawy**: 
  <a href="https://github.com/mariamelnemrawy" target="_blank">
    <img src="https://cdn.jsdelivr.net/npm/simple-icons@v9/icons/github.svg" alt="GitHub" width="20"/>
  </a>
  <a href="https://www.linkedin.com/in/mariam-elnemrawy-0213b92b5?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app" target="_blank">
    <img src="https://cdn.jsdelivr.net/npm/simple-icons@v9/icons/linkedin.svg" alt="LinkedIn" width="20"/>
  </a>

- **Mariam Ahmed Mohamed**: 
  <a href="https://github.com/engmariamahmed04" target="_blank">
    <img src="https://cdn.jsdelivr.net/npm/simple-icons@v9/icons/github.svg" alt="GitHub" width="20"/>
  </a>
  <a href="https://www.linkedin.com/in/mariam-a-hassan/" target="_blank">
    <img src="https://cdn.jsdelivr.net/npm/simple-icons@v9/icons/linkedin.svg" alt="LinkedIn" width="20"/>
  </a>

- **Eman Yasser Elnaggar**: 
  <a href="https://github.com/Eman-elnagggar/" target="_blank">
    <img src="https://cdn.jsdelivr.net/npm/simple-icons@v9/icons/github.svg" alt="GitHub" width="20"/>
  </a>
  <a href="https://www.linkedin.com/in/eman-elnaggar-6529a72b8/" target="_blank">
    <img src="https://cdn.jsdelivr.net/npm/simple-icons@v9/icons/linkedin.svg" alt="LinkedIn" width="20"/>
  </a>

- **Roaa Raafat Said**: 
  <a href="https://github.com/roaa-838" target="_blank">
    <img src="https://cdn.jsdelivr.net/npm/simple-icons@v9/icons/github.svg" alt="GitHub" width="20"/>
  </a>
  <a href="https://www.linkedin.com/in/roaa-raafat" target="_blank">
    <img src="https://cdn.jsdelivr.net/npm/simple-icons@v9/icons/linkedin.svg" alt="LinkedIn" width="20"/>
  </a>

## 📜 License
This project is licensed under the MIT License.

## 🤝 Contributing
Contributions are welcome! Feel free to fork the repo, create a new branch, and submit a pull request.
