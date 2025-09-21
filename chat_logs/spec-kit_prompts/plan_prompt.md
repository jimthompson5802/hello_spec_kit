static single web page that is the interface for a python backend.  web page buttons invoke backend logic via REST API calls.
 All operations occur in the Python backend. The frontend is a simple HTML page served by `Flask`.

`pytest` is the testing framework for the backend.

all dependencies are managed via `pip` and listed in `requirements.txt`.

Language is Python 3.12+
Primary libraries are `Flask` for the backend and `requests` for REST API calls.
No local storage
testing is done with `pytest`.
Target platform is macOS.
Project type is a single user web app with a python backend that runs locally.
There are no performance goals beyond reasonable responsiveness for a local app.
