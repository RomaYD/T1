document.getElementById('uploadButton').addEventListener('click', function() {
    const fileInput = document.getElementById('fileInput');
    const fileList = document.getElementById('fileList');

    // Очищаем предыдущий список файлов
    fileList.innerHTML = '';

    // Получаем выбранные файлы
    const files = fileInput.files;

    // Проверяем, есть ли выбранные файлы
    if (files.length === 0) {
        fileList.innerHTML = '<p>Пожалуйста, выберите файлы для загрузки.</p>';
        return;
    }

    // Отображаем список выбранных файлов
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
        formData.append('file', files[i], files[i].name); // Используйте 'files' как имя поля
    }

    const url = 'http://localhost:8000/sprints/upload';
    
    fetch(url, {
        method: 'POST', // Метод запроса
        body: formData
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Сеть ответила с ошибкой ' + response.status);
        }
        return response.json(); // Преобразуем ответ в JSON
    })
    .then(data => {
        // Обработка успешного ответа
        document.getElementById('response').innerText = 'Ответ от сервера: ' + JSON.stringify(data);
    })
    .catch(error => {
        // Обработка ошибок
        document.getElementById('response').innerText = 'Ошибка: ' + error.message;
    });
});
