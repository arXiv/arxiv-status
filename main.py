from status.factory import create_web_app

app = create_web_app()

if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True, host="0.0.0.0" port=init(os.environ.get("PORT",8080)))
