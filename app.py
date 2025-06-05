from flask import Flask, render_template

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for the about page
@app.route('/about')
def about():
    return render_template('about.html')

# Route for the projects page
@app.route('/projects')
def projects():
    # Example projects data
    project_list = [
        {
            'title': 'Project 1',
            'description': 'A cool project description.',
            'image': 'static/images/project1.jpg',
            'link': 'https://example.com' 
        },
        {
            'title': 'Project 2',
            'description': 'Another awesome project.',
            'image': 'static/images/project2.jpg',
            'link': 'https://example.com' 
        }
    ]
    return render_template('projects.html', projects=project_list)

if __name__ == '__main__':
    app.run(debug=True)