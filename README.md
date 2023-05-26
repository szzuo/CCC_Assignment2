# CCC_Assignment2
Group33 Assignment2

## Frontend website

(http://172.26.129.111:8501/)

The front-end of this project utilizes Streamlit, an open-source application framework, for constructing interactive, data-driven applications with Python scripts and supports complex objects and models. Streamlit is characterized by its real-time interactivity, expedited development process, and it simplifies the deployment of data-driven web applications. In this project, we optimized the efficiency of data requests from the backend by using Streamlit's internal plugins, thus improving user experience.



## Video
Part one： \url

Part two:  [![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/Cp7H8vrW6WE/0.jpg)](https://youtu.be/Cp7H8vrW6WE)

![alt text](./img/about_us.png)


## Architecture
![alt text](./img/logo.jpg)

## Deployment user guide
# CCC_Assignment2

## Setup and Execution with Ansible

This repository includes an Ansible script (`Ansible.yaml` in the `Data` folder) for setting up the required environment and running the Python application. The script automates the following tasks:

1. Install Python3
2. Install pip for Python3
3. Install Mastodon and CouchDB Python libraries using pip
4. Install Transformers library using pip
5. Install Scipy library using pip
6. Install PyTorch library using pip
7. Run the Python application `Mastodon.py` in a detached mode

To execute the Ansible script, navigate to the directory containing the script and run the following command in the terminal:

```bash
ansible-playbook Ansible.yaml
#### 4. Backend
```bash
pip3 install -r environment.txt

python3 main.py

