from flask import render_template, request

from models import Task


def register_routes(app, db):

    @app.route('/', methods=['GET', 'POST'])
    def index():
        print(request.method)
        if request.method == 'GET':
            tasks = Task.query.all()
            return render_template('index.html', tasks=tasks)
        elif request.method == 'POST':
            name = request.form.get('name')
            print(name)
            description = request.form.get('description')
            print(description)
            status = request.form.get('status')
            print(status)
            # deadline = request.form.get('deadline')

            new_task = Task(name=name, description=description, status=status)
            print(new_task)


            db.session.add(new_task)
            db.session.commit()
            # task.save_to_db()

            tasks = Task.query.all()
            print(tasks)
            return render_template('index.html', tasks=tasks)