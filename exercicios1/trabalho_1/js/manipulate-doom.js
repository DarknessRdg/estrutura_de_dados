const memorizeDiv = document.querySelector('#memorize');



const countDownDiv = document.querySelector('#countdown');
let count = 5;
let countDown = (nextFuntion, total) => setInterval(() => {
    countDownDiv.innerHTML = count;
    setProgress( count / total);

    count --;
    if (count === -1)
        nextFuntion();
}, 1000);

let countDownVar = countDown(startGame, 5);


function setProgress(percent) {
    percent = (100 - percent * 100).toFixed(0);
    const progressBar = document.querySelector('.progress-bar');
    progressBar.style.width = percent + '%';
    progressBar.setAttribute('aria-valuenow', percent);
}

function startGame() {
    clearInterval(countDownVar);
    document.querySelector('#countdown-content').remove();
    const memorize = document.querySelector('#memorize');

    setProgress(0);
    memorize.classList.remove('hide');
    createMemorizeList();

    count = 5;
    countDownVar = countDown(createMemorizeGame, 30);
}


function createMemorizeList() {
    document.querySelector('.progress').classList.remove('hide');
    const carousel = document.querySelector('#memorizeCarousel');
    const ol = carousel.querySelector('ol');
    const carouselImages = carousel.querySelector('.carousel-inner');

    for (let i = 0; i < QUANTITY_TO_MEMORYZE; i++) {
        let li = document.createElement('li');
        li.setAttribute('data-target', '#memorizeCarousel');
        li.setAttribute('data-slide-to', i);
        if (i === 0)
            li.classList.add('active');
        ol.appendChild(li);

        let div = document.createElement('div');
        div.classList.add('carousel-item');
        if (i === 0)
            div.classList.add('active');
        let img = document.createElement('img');
        img.setAttribute('src', listToMemorize.cellAt(i).imagePath);
        img.classList.add('rounded');
        img.classList.add('shadow-lg');

        div.appendChild(img);
        carouselImages.appendChild(div);
    }
}


function stillFreeToGo() {
    return listToMemorize.length !== 0;
}


function createMemorizeGame() {
    clearInterval(countDownVar);
    setProgress(0);
    document.querySelector('#memorize').classList.add('hide');

    if (stillFreeToGo()) {  // ainda tem imagem na lista de memorizar
        const createImage = (imgURL, imageName) => {
            let newImage = document.createElement('div');
            newImage.setAttribute('class', 'col-6 mt-4 mb-4');

            let img = document.createElement('img');
            img.setAttribute('src', imgURL);
            img.setAttribute('id', imageName);

            newImage.appendChild(img);
            return newImage;
        };

        document.querySelector('#memorize-game').classList.remove('hide');
        const mainDiv = document.querySelector('#memorize-game-items');
        mainDiv.innerHTML = '';

        let listToChoose = createListToChoose();
        for (let i = 0; i < listToChoose.length; i++) {
            let distractor =  listToChoose[i];
            let newImage = createImage(distractor.imagePath, distractor.image);
            console.log(newImage);
            mainDiv.appendChild(newImage);
        }

        clickImageListener();
        count = 5;
        countDownVar = countDown(createMemorizeGame, count);
    }
    else {   // nao tem mais imagem para memorizar
        finishGame();
    }
}


function finishGame() {
    const result = document.querySelector('#result');
    document.querySelector('#memorize-game').classList.add('hide');
    result.classList.remove('hide');
    result.classList.add('d-flex');
    clearInterval(countDownVar);

    result.querySelector('#points').innerHTML = String(points()) + '%';
    result.querySelector('#correct').innerHTML = corrects();
    result.querySelector('#wrong').innerHTML = wrongs();
}


function clickImageListener() {
    document.querySelectorAll('img').forEach(node => {
        node.addEventListener('click', (event) => {
            const img = event.path[0];
            const id = img.getAttribute('id');

            handleImageHit(id);
            createMemorizeGame()
        })
    })
}