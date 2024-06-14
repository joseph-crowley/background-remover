document.addEventListener('DOMContentLoaded', function () {
    let dropArea = document.querySelector('.container');
    let form = document.querySelector('form');
    let fileInput = document.querySelector('input[type="file"]');
    let spinner = document.getElementById('spinner');

    dropArea.addEventListener('dragover', function (e) {
        e.preventDefault();
        dropArea.classList.add('dragover');
    });

    dropArea.addEventListener('dragleave', function () {
        dropArea.classList.remove('dragover');
    });

    dropArea.addEventListener('drop', function (e) {
        e.preventDefault();
        dropArea.classList.remove('dragover');
        let files = e.dataTransfer.files;
        fileInput.files = files;
        if (fileInput.files.length > 0) {
            submitFormWithFile();
        }
    });

    form.addEventListener('submit', function (e) {
        e.preventDefault();
        if (fileInput.files.length > 0) {
            submitFormWithFile();
        }
    });

    function submitFormWithFile() {
        spinner.style.display = 'block';
        let formData = new FormData(form);
        fetch('/', {
            method: 'POST',
            body: formData
        }).then(response => response.text())
          .then(html => {
              document.open();
              document.write(html);
              document.close();
          }).catch(error => {
              console.error('Error:', error);
              spinner.style.display = 'none';
          });
    }
});

