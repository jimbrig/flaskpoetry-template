"""
Flask Application Module
"""

from src.app.app import create_app

__version__ = "1.0.0"
__author__ = "Jimmy Briggs"

if __name__ == "__main__":
    app = create_app()
    app.run
