window.addEventListener('load', function() {
    const url = 'http://localhost:8000/sprints/list';
    const data = {ids: [], dates: {
        from: '1970-01-01T10:05:08', // начальная дата в формате ISO 8601
        to: '1970-01-01T10:05:08'    // конечная дата в формате ISO 8601
    }};
    fetch(url, {
        method: 'POST',
        body: JSON.stringify(data),
        headers: {
            'Content-Type': 'application/json',
            'Access-Control-Request-Method': 'OPTIONS'
        },
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Сеть ответила с ошибкой ' + response.status);
        }

        return response.json();
    })
    .then(data => {
        data.JSON
        document.getElementById('content').appendChild(data.JSON)
        this.window.addEventListener('response').innerText = 'Ответ от сервера: ' + JSON.stringify(data);
    })
    .catch(error => {
        this.window.addEventListener('response').innerText = 'Ошибка: ' + error.message;
    });
});