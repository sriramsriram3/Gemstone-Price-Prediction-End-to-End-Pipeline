from flask import Flask,render_template,jsonify,request
from src.pipelines.prediction_pipeline import PredictPipeline,CustomData


app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("index.html")  # Render the home page

@app.route("/predict", methods=["GET", "POST"])
def predict_datapoint():
    if request.method == "GET":
        return render_template("form.html")  # Render the form for data input
    else:
        # Retrieve form data and create an instance of CustomData
        data = CustomData(
            carat=float(request.form.get("carat")),
            depth=float(request.form.get("depth")),
            table=float(request.form.get("table")),
            x=float(request.form.get("x")),
            y=float(request.form.get("y")),
            z=float(request.form.get("z")),
            cut=request.form.get("cut"),
            color=request.form.get("color"),
            clarity=request.form.get("clarity")
        )

        # Convert the data to a DataFrame
        final_data = data.get_data_as_dataframe()

        # Initialize the prediction pipeline
        predict_pipeline = PredictPipeline()

        # Make a prediction
        pred = predict_pipeline.predict(final_data)

        # Round the prediction result
        result = round(pred[0], 2)

        # Render the result page with the prediction
        return render_template("result.html", final_result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
