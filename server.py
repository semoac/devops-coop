from flask import Flask
import os

from coop import create_app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)