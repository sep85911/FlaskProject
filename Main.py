from App import flaskApp;

if __name__ == "__main__":
    appIns = flaskApp.create_app();

    with appIns.app_context():
        flaskApp.db.create_all();

    appIns.run();




