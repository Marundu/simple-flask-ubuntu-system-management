# To run apt, apt-get, reboot, and shutdown 
# without sudo asking for a password, 
# set NOPASSWD option in /etc/sudoers.tmp
# in the line below %sudo   ALL=(ALL:ALL) ALL
# with the format
# username ALL=(ALL) NOPASSWD: /usr/bin/apt,/usr/bin/apt-get,/sbin/shutdown,/sbin/reboot

from flask import Flask
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from webbrowser import open_new_tab
import os

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
    return redirect(url_for('home'))

@app.route('/upgrade', methods=['POST'])
def upgrade():
    upgrade=request.form.get('upgrade')
    flash('Your system will now upgrade.')
    os.system('sudo apt upgrade -y')
    flash('Upgrade complete!')
    return redirect(url_for('home'))

@app.route('/update_upgrade', methods=['POST'])
def update_upgrade():
    update_upgrade=request.form.get('update_upgrade')
    flash('Your system will now update and upgrade.')
    os.system('sudo apt upgrade -y && sudo apt upgrade -y')
    flash('Update and upgrade complete!')
    return redirect(url_for('home'))

@app.route('/clean', methods=['POST'])
def clean():
    clean=request.form.get('clean')
    flash('Your system will now be cleaned.')
    os.system('sudo apt-get autoclean -y')
    os.system('sudo apt-get autoremove -y')
    flash('Cleaning complete!')
    return redirect(url_for('home'))
        
@app.route('/reboot', methods=['POST'])
def reboot():
    reboot=request.form.get('reboot')
    flash('Your system will now reboot.')
    os.system('sudo reboot')

@app.route('/shutdown', methods=['POST'])
def shutdown():
    shutdown=request.form.get('shutdown')
    flash('Your system will now shut down.')
    os.system('sudo shutdown -h 0')

def generate_html_log():
    sys_log=open('/var/log/apt/term.log', 'r')
    html_log=open('html_logs/log.html', 'w')
   
    wrapper='<p>{}</p>'
    
    for line in sys_log:
        log_content=wrapper.format(line)
        html_log.write(log_content)
    html_log.close()
               
@app.route('/check_log', methods=['POST'])
def check_log():
    check_log=request.form.get('check_log')
    open_new_tab('html_logs/log.html')
    return redirect(url_for('home'))

@app.route('/generate', methods=['POST'])
def generate_log():
    generate_log=request.form.get('generate')
    generate_html_log()
    open_new_tab('html_logs/log.html')
    return redirect(url_for('home'))
    
if __name__=='__main__':
    app.run(debug=True, port=7097)
