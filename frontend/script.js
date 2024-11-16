document.getElementById('uploadButton').addEventListener('click', function() {
    const fileInput = document.getElementById('fileInput');
    const fileList = document.getElementById('fileList');

    fileList.innerHTML = '';

    const files = fileInput.files;

    if (files.length === 0) {
        fileList.innerHTML = '<p>Пожалуйста, выберите файлы для загрузки.</p>';
        return;
    }

    const ul = document.createElement('ul');
    for (let i = 0; i < files.length; i++) {
        const li = document.createElement('li');
        li.textContent = files[i].name;
        ul.appendChild(li);
    }
    
    fileList.appendChild(ul);
    const formData = new FormData();

    // Добавляем все выбранные файлы в FormData
    for (let i = 0; i < files.length; i++) {
        formData.append('file', files[i], files[i].name);
    }

    const url = 'http://localhost:8000/sprints/upload';

    fetch(url, {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Сеть ответила с ошибкой ' + response.status);
        }
        goToPage('page1.html');
        return response.json();
    })
    .then(data => {
        document.getElementById('response').innerText = 'Ответ от сервера: ' + JSON.stringify(data);
    })
    .catch(error => {
        document.getElementById('response').innerText = 'Ошибка: ' + error.message;
    });
});

function goToPage(page) {
    window.location.href = page;
}
