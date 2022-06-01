from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == "POST":
        
        rands = request.form['rands']
    
        if rands.isnumeric():
            rands = float(rands)
            vat = rands / 1.15

            if rands > 0: 
                rands = vat * 0.43 
                units = round(rands, 2)

            return render_template('index.html', rands=rands, units=units)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)