

## (keys)
chmod 400 /Users/path/xxxx.pem

## Access AWS 
ssh -i /Users/path/xxx.pem ec2-user@ec2-00-00-000-000.compute-1.amazonaws.com

# Install

## Linux
sudo yum update

### python
sudo yum install python3 python3-pip

### packages
pip3 install pandas selenium

### install Google Chrome on Amazon Linux 2:
sudo yum install -y wget unzip xorg-x11-server-Xvfb

#### Download the Google Chrome RPM package:
wget https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm

#### Install the Google Chrome package using yum:
sudo yum localinstall -y google-chrome-stable_current_x86_64.rpm

([ec2-user@ec2-000-00-00-000 ~]$ google-chrome --version
Google Chrome 112.0.5615.49 )


####  Install the Chrome WebDriver:
wget https://chromedriver.storage.googleapis.com/112.0.5615.49/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/local/bin/ 
sudo chmod +x /usr/local/bin/chromedriver

wget https://chromedriver.storage.googleapis.com/index.html?path=112.0.5615.49/#:~:text=chromedriver_linux64.zip

Note: The WebDriver version should match the version of Google Chrome installed on the EC2 instance. Check the Chrome version using google-chrome --version and download the appropriate WebDriver version from the official site.

#### Prepare scrip
service = Service('/usr/local/bin/chromedriver')

#### Transfer the script to the EC2 instance using SCP:
scp -i path/xxx.pem /Users/path/LSSP-project/bitcointalk_data.csv ec2-user@ip-000-00-00-000.compute-1.amazonaws.com:/home/ec2-user/

scp -i path/xxx.pem /Users/path//LSSP-project/process_1_aws.py ec2-user@ec2-000-00-00-000.compute-1.amazonaws.com:/home/ec2-user/

#### Multiple

scp -i path/xxx.pem path/LSSP-project/bitcointalk_data.csv /path/LSSP-project/bitcointalk/process_1_aws.py ec2-user@ec2-000-00-00-000.compute-1.amazonaws.com:/home/ec2-user/

### Checking
ssh -i path/xxx.pem ec2-user@ec2-000-00-00-000.compute-1.amazonaws.com
cd /home/ec2-user/
ls

### Transfer the output data:
scp -i path/xxx.pem ec2-user@your-instance-public-dns:/path/to/output_data /path/to/local_destination/

### for csv file 
scp -i path/xxx.pem /path/bitcointalk_data.csv ec2-user@ec2-000-00-00-000.compute-1.amazonaws.com:/home/ec2-user/

### Update the script to use the correct CSV file path:
scp -i path/xxx.pem /path/to/my_script.py ec2-user@ec2-000-00-00-000.compute-1.amazonaws.com:/home/ec2-user/

scp -i path/xxx.pem /path//LSSP-project/bitcointalk/multiprocess_btc_aws.py ec2-user@ec2-000-00-00-000.compute-1.amazonaws.com:/home/ec2-user/

### Run the script on the EC2 instance:
python3 process_1_aws.py

# checking

scp -i path/xxx.pem -r ec2-user@your-ec2-instance:/path/to/your/folder /path/to/your/local/folder

### Erasing

rm /home/ec2-user/process_1_aws.py
rm -r /home/ec2-user/output_data


### use tmux:

### Install

sudo yum install tmux.

Start a new tmux session by typing tmux in the terminal.

Run your Python script within the tmux session.

Detach from the tmux session by typing Ctrl-b d. 

This will return you to the regular terminal prompt.

Disconnect from the SSH connection.

To reconnect to the tmux session and check the status of your script, reconnect to the AWS instance 
using SSH and type tmux attach to reattach to the tmux session.






