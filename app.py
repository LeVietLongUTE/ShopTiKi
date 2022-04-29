from flask import Flask
# from DataModel.Customer import addCustomer
app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return "hello tôi là long abc"

# @app.route("/addCustomer",methods=["GET","POST"])
# def addCustomerRoute():
#     addCustomer()
#     return "addCustomer"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
