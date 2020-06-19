from flask import Flask, render_template, request, url_for, redirect
import cairosvg
from rdkit import Chem
from rdkit.Chem.Draw import rdMolDraw2D
import os
import base64
import io
import time
from PIL import Image

app = Flask(__name__, static_url_path='/static')

@app.route("/", methods = ['GET', 'POST'])
@app.route("/home", methods = ['GET', 'POST'])
def home():
    if request.method == 'POST':
        smiles = request.form.get('smiles')
        pdb = request.form.get('pdb')

        # Check if valid SMILES string
        try:
            mol = Chem.MolFromSmiles(smiles)
            can_smi = Chem.MolToSmiles(mol, True)
        except:
            can_smi = None
            pass

        if smiles == '' or pdb == '':
            return redirect(url_for('error'))

        # Check for Invalid string
        if can_smi is None or pdb is None:
            return redirect(url_for('error'))

        return redirect(url_for('default', smiles=smiles, pdb=pdb))

    return render_template('home.html')


@app.route("/error", methods=['GET', 'POST'])
def error():
    return render_template('error.html')


@app.route("/error_btn", methods=['GET', 'POST'])
def error_btn():
    return render_template('home.html')

@app.route("/default", methods=['GET', 'POST'])
def default():

    smiles = request.args.get('smiles', None)
    pdb = request.args.get('pdb', None)

    def smi_to_png(smi, query_smi_path, get_binary=False):
        mol = Chem.MolFromSmiles(smi)
        d2d = rdMolDraw2D.MolDraw2DSVG(300, 300)
        d2d.DrawMolecule(mol)
        d2d.FinishDrawing()
        svg_vector = d2d.GetDrawingText()
        cairosvg.svg2png(bytestring=svg_vector, write_to=query_smi_path + 'query_smi.png')

        img = Image.open(query_smi_path + 'query_smi.png', mode='r')
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format='PNG')
        encoded_img = base64.encodebytes(img_byte_arr.getvalue()).decode('ascii')
        return encoded_img

    binary_image = smi_to_png(smiles, './static/images/', get_binary=True)

    ############################################################################

    new_sdf_name = "query_smi" + str(time.time()) + ".sdf"
    for filename in os.listdir('static/'):
        if filename.startswith('query_smi'):  # not to remove other images
            os.remove('static/' + filename)

    w = Chem.SDWriter('static/' + new_sdf_name)
    m2 = Chem.MolFromSmiles(smiles)
    w.write(m2)

    ############################################################################

    return render_template('default.html', query_smi=smiles, binary_image=binary_image, sdf_file=new_sdf_name, pdb=pdb)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    # app.run(debug=True)
