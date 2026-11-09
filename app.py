import os
from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

tasks = []

HTML = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>TaskFlow</title>
</head>
<body>
    <h1>TaskFlow - Gerenciador de Tarefas</h1>
    <p>Deploy automático funcionando!</p>

    <form method="POST">
        <input type="text" name="task" placeholder="Nova tarefa" required>
        <button type="submit">Adicionar</button>
    </form>

    <h2>Minhas tarefas</h2>
    <ul>
        {% for task in tasks %}
            <li>{{ task }}</li>
        {% else %}
            <li>Nenhuma tarefa cadastrada.</li>
        {% endfor %}
    </ul>
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        task = request.form.get("task", "").strip()

        if task:
            tasks.append(task)

        return redirect("/")

    return render_template_string(HTML, tasks=tasks)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)