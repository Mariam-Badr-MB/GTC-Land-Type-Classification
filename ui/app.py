import streamlit as st
import numpy as np
from PIL import Image
import torch
import torch.nn as nn
import torchvision.transforms as transforms
import torchvision.models as models
import matplotlib.pyplot as plt

# ================== CONFIG ==================
MODEL_PATH = "models/best_efficientnet_b0_model.pth"
CLASS_NAMES = ["Agriculture", "Water", "Urban", "Desert", "Trees"]

st.set_page_config(
    page_title="🌍 Land Type Classification",
    page_icon="🌱",
    layout="wide",
)

# ================== MODEL ==================
@st.cache_resource
def load_trained_model():
    model = models.efficientnet_b0(pretrained=False)
    model.classifier = nn.Sequential(
        nn.Dropout(p=0.2),
        nn.Linear(1280, 512),
        nn.ReLU(),
        nn.Dropout(p=0.2),
        nn.Linear(512, len(CLASS_NAMES)) 
    )

    state_dict = torch.load(MODEL_PATH, map_location=torch.device("cpu"))
    from collections import OrderedDict
    new_state_dict = OrderedDict()
    for k, v in state_dict.items():
        if "classifier.4" not in k: 
            new_state_dict[k] = v
    model.load_state_dict(new_state_dict, strict=False)
    model.eval()
    return model

model = load_trained_model()

# ================== FUNCTIONS ==================
def preprocess_image(img: Image.Image):
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
    ])
    return transform(img).unsqueeze(0)

def plot_probabilities(probs, class_names):
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.barh(class_names, probs, color="skyblue")
    ax.set_xlim([0, 1])
    for i, v in enumerate(probs):
        ax.text(v + 0.01, i, f"{v*100:.1f}%", va="center")
    st.pyplot(fig)

# ================== UI ==================
st.markdown("<h1 style='text-align: center; color: #2c3e50;'>🌍 Land Type Classification</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Upload a Sentinel-2 satellite image and classify its land type.</p>", unsafe_allow_html=True)

uploaded_file = st.file_uploader("📂 Upload Image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    col1, col2 = st.columns([1, 2])

    with col1:
        image = Image.open(uploaded_file)
        st.image(image, caption="🖼 Uploaded Image", use_column_width=True)

    with col2:
        if st.button(" ** Predict ** ", use_container_width=True):
            x = preprocess_image(image)
            with torch.no_grad():
                preds = model(x)
                probs = torch.softmax(preds, dim=1)[0].numpy()
                top_idx = np.argmax(probs)

            st.success(f" **Prediction:** {CLASS_NAMES[top_idx]} ({probs[top_idx]*100:.1f}% confidence)")

            st.subheader("Class Probabilities")
            plot_probabilities(probs, CLASS_NAMES)

# ================== FOOTER ==================
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Developed with ❤️ using PyTorch & Streamlit</p>", unsafe_allow_html=True)
