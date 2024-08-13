const serchfun = () => {
    const serchText = document.getElementById('searchbox').value;
    window.location.href = "http://www.baidu.com/s?wd=" + serchText;
    serchText.value = '';
};

const serchfunBtn = () => {
    const btn = window.event.code;
    if (btn === 'Enter') {
        const serchText = document.getElementById('searchbox').value;
        window.location.href = "http://www.baidu.com/s?wd=" + serchText;
        serchText.value = '';
    }
};