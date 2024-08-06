from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)

todo_list = ToDoList()

@app.route('/')
def index():
    return render_template('index.html', tasks=todo_list.tasks)

@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    todo_list.add_task(task)
    app.logger.debug(request.form)
    app.logger.debug(todo_list.tasks)
    return redirect(url_for('index'))

@app.route('/remove/<task>')
def remove(task):
    todo_list.remove_task(task)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)