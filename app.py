# To run apt, apt-get, reboot, and shutdown 
# without sudo asking for a password, 
# set NOPASSWD option in /etc/sudoers.tmp
# in the line below %sudo   ALL=(ALL:ALL) ALL
# with the format
# username ALL=(ALL) NOPASSWD: /usr/bin/apt,/usr/bin/apt-get,/sbin/shutdown,/sbin/reboot

# Improvements - dump logs to html, add progress bar,
# install and uninstall programs via a text box,
# scheduled shutdowns and reboots

import os
from flask import Flask, flash, redirect, render_template, request, url_for
import webbrowser

app=Flask(__name__)
app.secret_key=os.urandom(50)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/update', methods=['POST'])
def update():
    update=request.form.get('update')
    flash('Your system will now update.')
    os.system('sudo apt update -y')
    flash('Update complete!')
    #html_log()
    return redirect(url_for('home'))

@app.route('/upgrade', methods=['POST'])
def upgrade():
    upgrade=request.form.get('upgrade')
    flash('Your system will now upgrade.')
    os.system('sudo apt upgrade -y')
    flash('Upgrade complete!')
    #html_log()
    return redirect(url_for('home'))
        
@app.route('/reboot', methods=['POST'])
def reboot():
    reboot=request.form.get('reboot')
    flash('Your system will now reboot.')
    os.system('sudo reboot')
    return redirect(url_for('home'))

@app.route('/shutdown', methods=['POST'])
def shutdown():
    shutdown=request.form.get('shutdown')
    flash('Your system will now shut down.')
    os.system('sudo shutdown -h 0')
    return redirect(url_for('home'))

def html_log():
    log='/var/log/apt/term.log'

    # Convert term.log to log.html:
    # each line in term.log to be <p><br>
            
# @app.route('/check_logs', methods=['GET','POST'])
# def check_logs():
#     check_logs=request.form.get('check_logs')
#     html_log()
#     webbrowser.open('html_logs/log.html')
    
if __name__=='__main__':
    app.run(debug=True, port=7097)
