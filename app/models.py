from app import db

class Users(db.Model):
    id = db.Column(db.String(100), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    def __repr__(self):
        return f'<User {self.name}>'

