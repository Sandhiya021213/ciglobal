# import os
# from flask import Flask, flash, render_template, request, redirect, url_for
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from datetime import datetime

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:sandy123@localhost/leaveapp'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SECRET_KEY'] = 'your_secret_key'

# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

# class LeaveRequest(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     employee_name = db.Column(db.String(100), nullable=False)
#     email = db.Column(db.String(100), nullable=False)
#     start_date = db.Column(db.Date, nullable=False)
#     end_date = db.Column(db.Date, nullable=False)
#     leave_type = db.Column(db.String(50), nullable=False)
#     reason = db.Column(db.Text, nullable=False)

# def send_email(to_email, leave_request):
#     from_email = 'your_email@example.com'
#     from_password = 'your_email_password'
    
#     subject = 'Leave Request Details'
#     body = f"""
#     Employee Name: {leave_request.employee_name}
#     Email: {leave_request.email}
#     Start Date: {leave_request.start_date.strftime('%Y-%m-%d')}
#     End Date: {leave_request.end_date.strftime('%Y-%m-%d')}
#     Leave Type: {leave_request.leave_type}
#     Reason: {leave_request.reason}
#     """
    
#     msg = MIMEMultipart()
#     msg['From'] = from_email
#     msg['To'] = to_email
#     msg['Subject'] = subject
#     msg.attach(MIMEText(body, 'plain'))
    
#     try:
#         with smtplib.SMTP('smtp.example.com', 587) as server:
#             server.starttls()
#             server.login(from_email, from_password)
#             server.send_message(msg)
#     except Exception as e:
#         print(f'Error: {e}')

# @app.route('/')
# def home():
#     return render_template('home.html')

# @app.route('/login')
# def login():
#     return render_template('login.html')

# @app.route('/dashboard')
# def dashboard():
#     return render_template('dashboard.html')

# @app.route('/leave_list')
# def leave_list():
#     leaves = LeaveRequest.query.all()
#     return render_template('leave_list.html', leaves=leaves)

# @app.route('/create_leave', methods=['GET', 'POST'])
# def create_leave():
#     if request.method == 'POST':
#         employee_name = request.form['employee_name']
#         email = request.form['email']
#         start_date = datetime.strptime(request.form['start_date'], '%Y-%m-%d').date()
#         end_date = datetime.strptime(request.form['end_date'], '%Y-%m-%d').date()
#         leave_type = request.form['leave_type']
#         reason = request.form['reason']

#         new_leave = LeaveRequest(employee_name=employee_name, email=email, start_date=start_date, end_date=end_date, leave_type=leave_type, reason=reason)
#         db.session.add(new_leave)
#         db.session.commit()
#         flash('Leave request created successfully!', 'success')
#         return redirect(url_for('leave_list'))
#     return render_template('create_leave.html')

# @app.route('/update_leave/<int:id>', methods=['GET', 'POST'])
# def update_leave(id):
#     leave = LeaveRequest.query.get_or_404(id)
#     if request.method == 'POST':
#         leave.employee_name = request.form['employee_name']
#         leave.email = request.form['email']
#         leave.start_date = datetime.strptime(request.form['start_date'], '%Y-%m-%d').date()
#         leave.end_date = datetime.strptime(request.form['end_date'], '%Y-%m-%d').date()
#         leave.leave_type = request.form['leave_type']
#         leave.reason = request.form['reason']

#         db.session.commit()
#         flash('Leave request updated successfully!', 'success')
#         return redirect(url_for('leave_list'))
#     return render_template('update_leave.html', leave=leave)

# @app.route('/delete_leave/<int:id>', methods=['POST'])
# def delete_leave(id):
#     leave = LeaveRequest.query.get_or_404(id)
#     if request.method == 'POST':
#         db.session.delete(leave)
#         db.session.commit()
#         flash('Leave request deleted successfully!', 'success')
#         return redirect(url_for('leave_list'))
#     return render_template('delete_leave.html', leave=leave)

# @app.route('/send_leave_email/<int:id>', methods=['POST'])
# def send_leave_email(id):
#     leave = LeaveRequest.query.get_or_404(id)
#     recipient_email = request.form['recipient_email']
    
#     send_email(recipient_email, leave)
    
#     flash('Email sent successfully!', 'success')
#     return redirect(url_for('leave_list'))

# if __name__ == '__main__':
#     app.run(debug=True, port=8080)




















# import os
# from flask import Flask, flash, render_template, request, redirect, url_for
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from flask_mail import Mail, Message
# from dotenv import load_dotenv
# from datetime import datetime

# load_dotenv()

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:sandy123@localhost/leaveapp'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SECRET_KEY'] = 'your_secret_key'

# app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
# app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT'))
# app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
# app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
# app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS') == 'True'
# app.config['MAIL_USE_SSL'] = os.getenv('MAIL_USE_SSL') == 'True'

# db = SQLAlchemy(app)
# migrate = Migrate(app, db)
# mail = Mail(app)

# class LeaveRequest(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     employee_name = db.Column(db.String(100), nullable=False)
#     email = db.Column(db.String(100), nullable=False)
#     start_date = db.Column(db.Date, nullable=False)
#     end_date = db.Column(db.Date, nullable=False)
#     leave_type = db.Column(db.String(50), nullable=False)
#     reason = db.Column(db.Text, nullable=False)

# def send_email(to_email, leave_request):
#     subject = 'Leave Request Details'
#     body = f"""
#     Employee Name: {leave_request.employee_name}
#     Email: {leave_request.email}
#     Start Date: {leave_request.start_date.strftime('%Y-%m-%d')}
#     End Date: {leave_request.end_date.strftime('%Y-%m-%d')}
#     Leave Type: {leave_request.leave_type}
#     Reason: {leave_request.reason}
#     """
    
#     msg = Message(subject, recipients=[to_email])
#     msg.body = body
    
#     try:
#         mail.send(msg)
#     except Exception as e:
#         print(f'Error: {e}')

# @app.route('/')
# def home():
#     return render_template('home.html')

# @app.route('/login')
# def login():
#     return render_template('login.html')

# @app.route('/dashboard')
# def dashboard():
#     return render_template('dashboard.html')

# @app.route('/leave_list')
# def leave_list():
#     leaves = LeaveRequest.query.all()
#     return render_template('leave_list.html', leaves=leaves)

# @app.route('/create_leave', methods=['GET', 'POST'])
# def create_leave():
#     if request.method == 'POST':
#         employee_name = request.form['employee_name']
#         email = request.form['email']
#         start_date = datetime.strptime(request.form['start_date'], '%Y-%m-%d').date()
#         end_date = datetime.strptime(request.form['end_date'], '%Y-%m-%d').date()
#         leave_type = request.form['leave_type']
#         reason = request.form['reason']

#         new_leave = LeaveRequest(employee_name=employee_name, email=email, start_date=start_date, end_date=end_date, leave_type=leave_type, reason=reason)
#         db.session.add(new_leave)
#         db.session.commit()
#         flash('Leave request created successfully!', 'success')
#         return redirect(url_for('leave_list'))
#     return render_template('create_leave.html')

# @app.route('/update_leave/<int:id>', methods=['GET', 'POST'])
# def update_leave(id):
#     leave = LeaveRequest.query.get_or_404(id)
#     if request.method == 'POST':
#         leave.employee_name = request.form['employee_name']
#         leave.email = request.form['email']
#         leave.start_date = datetime.strptime(request.form['start_date'], '%Y-%m-%d').date()
#         leave.end_date = datetime.strptime(request.form['end_date'], '%Y-%m-%d').date()
#         leave.leave_type = request.form['leave_type']
#         leave.reason = request.form['reason']

#         db.session.commit()
#         flash('Leave request updated successfully!', 'success')
#         return redirect(url_for('leave_list'))
#     return render_template('update_leave.html', leave=leave)

# @app.route('/delete_leave/<int:id>', methods=['POST'])
# def delete_leave(id):
#     leave = LeaveRequest.query.get_or_404(id)
#     if request.method == 'POST':
#         db.session.delete(leave)
#         db.session.commit()
#         flash('Leave request deleted successfully!', 'success')
#         return redirect(url_for('leave_list'))
#     return render_template('delete_leave.html', leave=leave)

# @app.route('/send_leave_email/<int:id>', methods=['POST'])
# def send_leave_email(id):
#     leave = LeaveRequest.query.get_or_404(id)
#     recipient_email = request.form['recipient_email']
    
#     send_email(recipient_email, leave)
    
#     flash('Email sent successfully!', 'success')
#     return redirect(url_for('leave_list'))

# if __name__ == '__main__':
#     app.run(debug=True, port=8080)







import os
from flask import Flask, flash, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail, Message
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:sandy123@localhost/leaveapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'

# Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = os.getenv('MAIL_USE_SSL') == 'True'

db = SQLAlchemy(app)
migrate = Migrate(app, db)
mail = Mail(app)

# Model for Leave Request
class LeaveRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    leave_type = db.Column(db.String(50), nullable=False)
    reason = db.Column(db.Text, nullable=False)

# Send email function using Flask-Mail
def send_email(to_email, leave_request):
    subject = 'Leave Request Details'
    body = f"""
    Employee Name: {leave_request.employee_name}
    Email: {leave_request.email}
    Start Date: {leave_request.start_date.strftime('%d-%m-%Y')}
    End Date: {leave_request.end_date.strftime('%d-%m-%Y')}
    Leave Type: {leave_request.leave_type}
    Reason: {leave_request.reason}
    """
    
    msg = Message(subject, sender=os.getenv('MAIL_USERNAME'), recipients=[to_email])
    msg.body = body
    
    try:
        mail.send(msg)
        print(f"Email sent successfully to {to_email}")
    except Exception as e:
        print(f'Error: {e}')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/leave_list')
def leave_list():
    leaves = LeaveRequest.query.all()
    return render_template('leave_list.html', leaves=leaves)

@app.route('/create_leave', methods=['GET', 'POST'])
def create_leave():
    if request.method == 'POST':
        employee_name = request.form['employee_name']
        email = request.form['email']
        start_date = datetime.strptime(request.form['start_date'], '%Y-%m-%d').date()
        end_date = datetime.strptime(request.form['end_date'], '%Y-%m-%d').date()
        leave_type = request.form['leave_type']
        reason = request.form['reason']

        new_leave = LeaveRequest(employee_name=employee_name, email=email, start_date=start_date, end_date=end_date, leave_type=leave_type, reason=reason)
        db.session.add(new_leave)
        db.session.commit()
        flash('Leave request created successfully!', 'success')
        return redirect(url_for('leave_list'))
    return render_template('create_leave.html')

@app.route('/update_leave/<int:id>', methods=['GET', 'POST'])
def update_leave(id):
    leave = LeaveRequest.query.get_or_404(id)
    if request.method == 'POST':
        leave.employee_name = request.form['employee_name']
        leave.email = request.form['email']
        leave.start_date = datetime.strptime(request.form['start_date'], '%Y-%m-%d').date()
        leave.end_date = datetime.strptime(request.form['end_date'], '%Y-%m-%d').date()
        leave.leave_type = request.form['leave_type']
        leave.reason = request.form['reason']

        db.session.commit()
        flash('Leave request updated successfully!', 'success')
        return redirect(url_for('leave_list'))
    return render_template('update_leave.html', leave=leave)

@app.route('/delete_leave/<int:id>', methods=['POST'])
def delete_leave(id):
    leave = LeaveRequest.query.get_or_404(id)
    if request.method == 'POST':
        db.session.delete(leave)
        db.session.commit()
        flash('Leave request deleted successfully!', 'success')
        return redirect(url_for('leave_list'))
    return render_template('delete_leave.html', leave=leave)

@app.route('/send_leave_email/<int:id>', methods=['POST'])
def send_leave_email(id):
    leave = LeaveRequest.query.get_or_404(id)
    recipient_email = request.form['recipient_email']
    
    send_email(recipient_email, leave)
    
    flash('Email sent successfully!', 'success')
    return redirect(url_for('leave_list'))

if __name__ == '__main__':
    app.run(debug=True, port=8080)

