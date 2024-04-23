from flask import render_template, request

from models import Task


def register_routes(app, db):
    @app.route('/', methods=['GET', 'POST'])
    def index():
        """
        Handles requests to the root URL.

        GET: Renders the index page with all tasks.
        POST: Adds a new task to the database and renders the index page with updated task list.

        Returns:
            render_template: HTML template rendered with tasks data.
        """
        if request.method == 'GET':
            tasks = Task.query.all()
            return render_template('index.html', tasks=tasks)
        elif request.method == 'POST':
            name = request.form.get('name')
            description = request.form.get('description')
            status = request.form.get('status')

            new_task = Task(name=name, description=description, status=status)
            new_task.save_to_db()

            tasks = Task.query.all()
            return render_template('index.html', tasks=tasks)
