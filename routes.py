from flask import render_template, request, redirect, url_for
from models import db, Task

# Endpoints
def init_routes(app):
    #List tasks
    @app.route("/")
    def index():
        tasks = Task.query.all()
        return render_template("index.html", tasks=tasks)
    #Add a task
    @app.route("/add", methods=["POST"])
    def add_task():
        task_content = request.form.get("content")
        if task_content:
            new_task = Task(content=task_content)
            db.session.add(new_task)
            db.session.commit()
        return redirect(url_for("index"))
    #Delete a task
    @app.route("/delete/<int:id>")
    def delete_task(id):
        task = Task.query.get(id)
        if task:
            db.session.delete(task)
            db.session.commit()
        return redirect(url_for("index"))
    #Completed task check
    @app.route("/complete/<int:id>")
    def complete_task(id):
        task = Task.query.get(id)
        if task:
            task.completed = not task.completed
            db.session.commit()
        return redirect(url_for("index"))