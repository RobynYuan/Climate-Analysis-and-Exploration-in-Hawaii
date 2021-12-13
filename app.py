# 1. Import Flask
from flask import Flask
# 2. Create an app
app = Flask(__name__)
# 3. Define static routes
@app.route("/")
def index():
    return(f"/api/v1.0/precipitation"
             "/api/v1.0/precipitation")
    # return(f"/api/v1.0/stations")
    # return(f"/api/v1.0/tobs")
    # return(f"/api/v1.0/<start> and /api/v1.0/<start>/<end>")

# 4. Define main behavior
if __name__ == "__main__":
    app.run(debug=True)




