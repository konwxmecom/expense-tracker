from app import create_app, db
from app.models import User

app = create_app()

# Database tables create karne ke liye shell command
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User}

if __name__ == '__main__':
    # Database create karo (agar nahi bani toh)
    with app.app_context():
        db.create_all()
        print('✅ Database tables created!')
    
    app.run(debug=True, port=5000)