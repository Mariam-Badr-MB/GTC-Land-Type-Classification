# GTC-Land-Type-Classification
## Project 14: Land Type Classification using Sentinel-2 Satellite Images

This project develops a machine learning model to classify land cover types in Egypt 
using Sentinel-2 satellite imagery. The system detects categories such as agriculture, 
water bodies, urban areas, deserts, roads, and tree cover. 

The workflow includes data preparation, exploratory analysis, model training & validation, 
and deployment through a lightweight web app. Final deliverables are a trained model, 
performance report, and an interactive application for testing land classification.

# Collaborators 
* Data Pipeline --> Mariam Badr & Roaa Raafat
* EDA & Feature engineering --> Roaa Raafat &
* Model Architecture --> Mariam Mohamed
* Evaluation & Explainability -->
* Deployment & dashboard --> Mariam Badr & 


# Dataset 
https://www.kaggle.com/datasets/apollo2506/eurosat-dataset

# Workflow
1- Data Pipeline (GTC_01_data_pipeline.ipynb + src/data_pipeline.py)
* Downloads & organizes EuroSAT dataset
* Cleans CSVs, ensures consistent labels
* Generates dataset statistics & class maps
* Outputs train/validation/test splits

2-Exploratory Data Analysis (GTC_02_eda_visualization.ipynb)
* Class distribution plots
* Sample images per class (grid view)
* Checks for corrupted/missing/duplicate images
* RGB intensity histograms
* Data augmentation visualizations (rotation, flips, jitter, crop/zoom)
* Class-level mean RGB statistics
* Feature extraction (color histograms, texture descriptors)
  
3- Feature Engineering (src/features.py)
* Geospatial-safe augmentations (rotation, flip, jitter, crop/zoom)
* Normalization & preprocessing utilities


# Outputs Generated
* train.csv, validation.csv, test.csv (cleaned datasets)
* dataset_statistics.json & plots (dataset_statistics.png, sample_images.png)
* augmentation_examples.png
* Engineered features in data/features/

# ⚡ Quick Start (Colab) - How to run? 
* step 1. Clone the repo
  ``!git clone https://github.com/Mariam-Badr-MB/GTC-Land-Type-Classification.git
      %cd GTC-Land-Type-Classification``
  
* step 2. Install dependencies
  ```!pip install kaggle seaborn matplotlib pillow torchvision```

* step 3. go to kaggle and Configure Kaggle API (for dataset download) & Upload your kaggle.json (from Kaggle account settings → API tokens):
  ``from google.colab import files, os
      uploaded = files.upload()  # upload kaggle.json
      !mkdir -p ~/.kaggle
      !cp kaggle.json ~/.kaggle/
      !chmod 600 ~/.kaggle/kaggle.json``

* step 4. Run the Data Pipeline GTC_01_data_pipeline.ipynb
* step 5. Run EDA & Visualization GTC_02_eda_visualization
# presentation (canva link)
https://www.canva.com/design/DAG0Dh60JoA/yx_ZVqEv5-SEXtxBMFXqUg/edit?utm_content=DAG0Dh60JoA&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton
