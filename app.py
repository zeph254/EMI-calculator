from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate_emi():
    try:
        # Get form data
        principal = float(request.form['principal'])
        annual_rate = float(request.form['annual_rate'])
        years = int(request.form['years'])
        
        # Convert to monthly values
        monthly_rate = annual_rate / 12 / 100
        months = years * 12
        
        # Calculate EMI using the formula
        emi = (principal * monthly_rate * math.pow(1 + monthly_rate, months)) / (math.pow(1 + monthly_rate, months) - 1)
        
        # Calculate total payment and total interest
        total_payment = emi * months
        total_interest = total_payment - principal
        
        # Prepare response
        result = {
            'emi': round(emi, 2),
            'total_payment': round(total_payment, 2),
            'total_interest': round(total_interest, 2),
            'principal': principal,
            'months': months
        }
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Add this at the bottom of your existing app.py
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=False)