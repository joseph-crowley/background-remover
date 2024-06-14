# Background Remover

This project is a Flask web application that allows users to remove the background from images using the `rembg` library. The application is Dockerized for easy deployment and portability. Based on Beyond Fireship's ["How I deploy serverless containers for free"](https://youtu.be/cw34KMPSt4k)

## Features

- Upload images directly through the web interface.
- Drag-and-drop support for easy image uploads.
- Displays a spinner while processing the image.
- Downloads the resulting image with the background removed.
- Dockerized for easy deployment and scaling.
- Comprehensive logging and error handling.

## Technologies Used

- Flask
- rembg
- Pillow
- Docker
- Bootstrap (for styling)
- JavaScript (for client-side functionality)

## Prerequisites

- Docker and Docker Compose installed on your system.

## Getting Started

### Clone the Repository

```bash
git clone git@github.com:joseph-crowley/background-remover.git
cd background-remover
```

### Build and Run the Docker Container

```bash
docker-compose up --build
```

### Access the Application

Open your browser and go to `http://localhost:8000`.

## Directory Structure

```
rembg-app/
├── app/
│   ├── static/
│   │   └── scripts.js
│   ├── templates/
│   │   └── index.html
│   ├── __init__.py
│   ├── main.py
│   └── requirements.txt
├── Dockerfile
└── docker-compose.yml
```

## File Descriptions

### `app/__init__.py`

Initializes the Flask application and configures logging.

### `app/main.py`

Defines the main route for handling GET and POST requests. It processes the uploaded image to remove the background using the `rembg` library.

### `app/templates/index.html`

Provides the HTML template for the application's web interface, including a form for file uploads, a drag-and-drop area, and a spinner for processing indication.

### `app/static/scripts.js`

Contains JavaScript to enhance the user experience by adding drag-and-drop functionality and displaying a spinner during image processing.

### `app/requirements.txt`

Lists the Python dependencies required for the application.

### `Dockerfile`

Defines the Docker image for the application, specifying the base image, environment variables, working directory, dependencies, and the command to run the Flask application.

### `docker-compose.yml`

Defines the Docker Compose configuration, setting up the service, ports, volumes, and environment variables.

## Environment Variables

- `FLASK_APP`: The Flask application name.
- `FLASK_ENV`: The environment mode for Flask (development/production).

## Logging

The application logs important events and errors to a file named `app.log`. The logs include timestamps, log levels, and messages.

## Security Considerations

- Ensure file uploads are validated to prevent malicious uploads.
- Use HTTPS in production to secure data transmission.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes. Ensure your code follows best practices and includes necessary tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- The [rembg](https://github.com/danielgatis/rembg) library for background removal.
- The [Flask](https://flask.palletsprojects.com/) framework for the web application.
- [Bootstrap](https://getbootstrap.com/) for styling.

## Contact

For questions or feedback, please contact Joseph Crowley at joseph.crowley@example.com.
