from flask import Flask, render_template, request
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

app = Flask(__name__)

# Mock data for demonstration purposes
stored_data = {
    '12345': {'field1': 'Value from PDF', 'field2': 'Another Value'}
}

@app.route('/form/<work_order>', methods=['GET'])
def form(work_order):
    data = stored_data.get(work_order, {})
    return render_template('form.html', data=data)

@app.route('/submit_form', methods=['POST'])
def submit_form():
    data = request.form
    create_pdf(data)
    return "Form submitted and PDF generated successfully"

def create_pdf(data):
    c = canvas.Canvas("output.pdf", pagesize=letter)
    c.drawString(100, 750, f"Field 1: {data['field1']}")
    c.drawString(100, 730, f"Field 2: {data['field2']}")
    c.save()

if __name__ == "__main__":
    app.run(debug=True)
