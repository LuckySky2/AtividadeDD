from flask import Flask, request, render_template

form = Flask(__name__)

@form.route('/')
def insira():
    return render_template('form.html')

@form.route('/soma', methods=['GET', 'POST'])
def soma():
    if request.method == 'POST':
        n1 = float(request.form['n1'])
        n2 = float(request.form['n2'])
        n3 = float(request.form['n3'])
        mult = n1*n2*n3
        return f"O resultado dos números multiplicados é: {mult}"
    else:
        return "ERRO: TENTE NOVAMENTE"

if __name__ == '__main__':
    form.run(debug=True)