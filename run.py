from flask import Flask, render_template, request, redirect, url_for
from forms import IndexForm
app = Flask(__name__)
app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'

@app.route("/", methods=["GET", "post"])
def show_index():
    form = IndexForm()
    if form.validate_on_submit():
        personal = form.personal.data
        mes = form.mes.data
        anio = form.anio.data
        next = request.args.get('next', None)
        if next:
            return redirect(next)
        return "¡Puedes descargar el archivo desde!"
    return render_template("index.html", form=form)
