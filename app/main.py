import io
import base64
from flask import Blueprint, request, render_template, send_file, flash, redirect, url_for, current_app as app
from rembg import remove
from PIL import Image

bp = Blueprint('main', __name__)

@bp.route('/', methods=['GET', 'POST'])
def index():
    """
    Handle the main route for GET and POST requests.
    """
    result = None
    if request.method == 'POST':
        app.logger.info('POST request received')
        if 'file' not in request.files:
            app.logger.warning('No file part')
            flash('No file part', 'danger')
            return redirect(url_for('main.index'))
        
        file = request.files['file']
        if file.filename == '':
            app.logger.warning('No selected file')
            flash('No selected file', 'danger')
            return redirect(url_for('main.index'))
        
        app.logger.info(f'Processing file: {file.filename}')
        
        try:
            input_image = Image.open(file)
            output_image = remove(input_image)
            output_io = io.BytesIO()
            output_image.save(output_io, format='PNG')
            output_io.seek(0)
            result = base64.b64encode(output_io.getvalue()).decode('ascii')
            app.logger.info('Background removed successfully')
            return render_template('index.html', result=result)
        except Exception as e:
            app.logger.error(f'An error occurred: {str(e)}')
            flash(f'An error occurred: {str(e)}', 'danger')
            return redirect(url_for('main.index'))
    return render_template('index.html', result=result)

