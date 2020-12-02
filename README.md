# Item Catalog Web App
This application is a part of Udacity's [IoT Software Foundation Nanodegree](https://in.udacity.com/course/iot-software-foundation-nanodegree--nd501-iniot).
This project is also connected to the [Full Stack Foundations](https://classroom.udacity.com/courses/ud088) and [Authentication and Authorization](https://classroom.udacity.com/courses/ud330) courses of Udacity. 

## About this project 
The Item Catalog project consists of developing an application that provides a list of items within a variety of categories, as well as provide a user registration and authentication system.

It is basically a RESTful web application using the Python framework Flask along with third-party OAuth authentication. It uses various HTTP methods which relate to CRUD (create, read, update and delete) operations on an SQL database.

### Installation

1. Install [Vagrant](https://www.vagrantup.com/) & [VirtualBox](https://www.virtualbox.org/wiki/Downloads).
2. Clone the [Udacity Vagrantfile](https://github.com/udacity/fullstack-nanodegree-vm)
3. Go to Vagrant directory and either clone this repo or download and place zip
3. Launch the Vagrant VM (`vagrant up`)
4. Log into Vagrant VM (`vagrant ssh`)
5. Navigate to `cd/vagrant`
6. Add required categories in `categories.csv` file(Or use the existing categories).
7. Add required items with category ID in `items.csv` file(Or use the existing items).
8. Setup application database using `python database_setup.py`
9. Populate the database with data using`python csv_data_upload.py`
10. Run application using `python project.py`
11. Access the application locally using http://localhost:8000
