import gradio as gr
import pandas as pd
import joblib
from pathlib import Path

# ---------------------------
# Model yuklash
# ---------------------------
MODEL_PATH = Path("Models/Random_Forest.joblib")
model = joblib.load(MODEL_PATH)

# ---------------------------
# Predict function
# ---------------------------
def predict_num_orders(
    center_id,
    checkout_price,
    base_price,
    emailer_for_promotion,
    homepage_featured,
    category,
    cuisine,
    price_diff,
    price_diff_ratio,
    price_diff_log,
    checkout_price_log,
    base_price_log,
    num_orders_sqrt
):
    df = pd.DataFrame([{
        "center_id": center_id,
        "checkout_price": checkout_price,
        "base_price": base_price,
        "emailer_for_promotion": emailer_for_promotion,
        "homepage_featured": homepage_featured,
        "category": category,
        "cuisine": cuisine,
        "price_diff": price_diff,
        "price_diff_ratio": price_diff_ratio,
        "price_diff_log": price_diff_log,
        "checkout_price_log": checkout_price_log,
        "base_price_log": base_price_log,
        "num_orders_sqrt": num_orders_sqrt
    }])

    prediction = float(model.predict(df)[0])
    return round(prediction, 2)

# ---------------------------
# Dashboard
# ---------------------------
with gr.Blocks(title="🍽️ Food Demand Prediction Dashboard") as demo:
    gr.Markdown(
        "# 🍽️ Food Demand Prediction\n"
        "RandomForest modeli orqali **buyurtmalar soni (num_orders)** ni bashorat qilish"
    )

    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("### 📦 Product & Center Info")
            center_id = gr.Number(label="Center ID", value=10, precision=0)
            category = gr.Number(label="Category", value=3, precision=0)
            cuisine = gr.Number(label="Cuisine", value=5, precision=0)

        with gr.Column(scale=1):
            gr.Markdown("### 💰 Pricing Info")
            checkout_price = gr.Number(label="Checkout Price", value=250.0)
            base_price = gr.Number(label="Base Price", value=300.0)
            price_diff = gr.Number(label="Price Difference", value=-50.0)
            price_diff_ratio = gr.Number(label="Price Diff Ratio", value=-0.16)
            price_diff_log = gr.Number(label="Price Diff Log", value=3.9)
            checkout_price_log = gr.Number(label="Checkout Price Log", value=5.52)
            base_price_log = gr.Number(label="Base Price Log", value=5.70)

        with gr.Column(scale=1):
            gr.Markdown("### 📣 Promotion Info")
            emailer_for_promotion = gr.Number(label="Emailer For Promotion (0/1)", value=1, precision=0)
            homepage_featured = gr.Number(label="Homepage Featured (0/1)", value=0, precision=0)
            num_orders_sqrt = gr.Number(label="Num Orders √ (historical)", value=10.0)

    # Predict button & output
    predict_btn = gr.Button("Predict 📊", variant="primary")
    output = gr.Number(label="🛒 Predicted Number of Orders", interactive=False)

    predict_btn.click(
        fn=predict_num_orders,
        inputs=[
            center_id,
            checkout_price,
            base_price,
            emailer_for_promotion,
            homepage_featured,
            category,
            cuisine,
            price_diff,
            price_diff_ratio,
            price_diff_log,
            checkout_price_log,
            base_price_log,
            num_orders_sqrt
        ],
        outputs=output
    )

    gr.Markdown("---\nBuilt by **Rasulbek AI** | RandomForestRegressor | Food Demand ML")

# ---------------------------
# Launch
# ---------------------------
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860, share=True)
