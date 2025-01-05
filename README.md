# My Flask Backend

This is a simple Flask backend application.

## Project Structure

```
my-flask-backend
├── app
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   └── templates
│       └── index.html
├── config.py
├── run.py
├── requirements.txt
└── README.md
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd my-flask-backend
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

To run the Flask application, execute the following command:
```
python run.py
```

The application will be available at `http://127.0.0.1:5000`.

## Usage

You can access the main page by navigating to `http://127.0.0.1:5000` in your web browser.

## License

This project is licensed under the MIT License.