from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost/alunos_db'
db = SQLAlchemy(app)

class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    ra = db.Column(db.String(20), unique=True, nullable=False)

@app.route('/cadastro', methods=['POST'])
def cadastrar_aluno():
    nome = request.form['nome']
    ra = request.form['ra']
    novo_aluno = Aluno(nome=nome, ra=ra)
    try:
        db.session.add(novo_aluno)
        db.session.commit()
        return jsonify({"message": "Aluno cadastrado"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": str(e)}), 500

@app.route('/metrics')
def metrics():
    return 'Métricas:'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

