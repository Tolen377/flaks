from main import create_app
from flask import redirect, url_for
app = create_app()
app.app_context().push()

@app.route('/')
def root():
    return redirect(url_for('page.home'))

if __name__ == '__main__':
    app.run(debug=True)    