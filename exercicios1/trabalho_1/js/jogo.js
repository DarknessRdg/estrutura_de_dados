let images = [
    'army', 'basket-ball', 'bike', 'bike-competition',
    'bird', 'church', 'concert', 'football', 'football-ball',
    'footbal-player', 'girl-shower', 'girl-yellow', 'guitar',
    'horses', 'judo', 'motorcycle', 'mountains', 'oriental-street',
    'person-reading', 'programing', 'red-car', 'sparks', 'temple',
    'tennis-ball', 'tower', 'trees', 'wedding', 'coffee', 'turtle',
    'space', 'drone', 'lemons', 'fox', 'waterfall', 'castle', 'lion',
    'cellphone', 'surf'
];
let imageArraySize = 38;


const QUANTITY_TO_MEMORYZE = 15;  // quantidade de imagens que o jogador tem que memorizar

const listToMemorize = createRandomList(QUANTITY_TO_MEMORYZE);  // lista com as imagens selecionadas que o
// jogador deve memorizar

const listOfImageLeft = parseArrayToList(images, imageArraySize);  // lista das imagens que NÃO foram selecionadas
// para memorizar
listToMemorize.show();


let rightImages = new Lista();  // lista com as imagens acertadas
let wrongImage = new Lista();  // lista com as imagens erradas


function createRandomList(quantity) {
    let lista = new Lista();

    for (let i = 0; i < quantity; i++) {
        let randomNumber = parseInt(Math.random() * imageArraySize);
        let imageName = removeFromImage(randomNumber);
        console.log('ADD: ' + imageName);
        lista.add(imageName);
    }
    return lista;
}


function removeFromImage(index) {
    const removed  = images[index];
    for (let i = index; i < imageArraySize - 1; i++) {
        images[i] = images[i + 1];
    }

    imageArraySize -= 1;
    return removed;
}


function parseArrayToList(array, arraySize) {
    let lista = new Lista();
    for (let i = 0; i < arraySize; i++)
        lista.add(array[i]);

    return lista;
}



let currentRightImage;
function createListToChoose() {
    let arrayOfCell = [];

    let randomIndex = parseInt(Math.random() * listToMemorize.length);
    let corretCell = listToMemorize.remove(randomIndex);

    currentRightImage = corretCell;
    arrayOfCell.push(corretCell);

    for (let i = 0; i < 5; i ++) {
        randomIndex = parseInt(Math.random() * listOfImageLeft.length);
        let wrongCell = listOfImageLeft.get(randomIndex);

        let areadyInArray = false;
        for (let j = 0; j < arrayOfCell.length && !areadyInArray; j++) {

            if (arrayOfCell[j].image === wrongCell.image)
                areadyInArray = true;
        }

        if (areadyInArray)
            i --;
        else
            arrayOfCell.push(wrongCell);
    }

    listToMemorize.show();
    return shuffle(arrayOfCell);
}


function handleImageHit(image) {
    const acert = hitCorrect(image);
    if (acert)
        rightImages.add(image);
    else
        wrongImage.add(image);
}


function hitCorrect(imageName) {
    return imageName === currentRightImage.image;
}


function shuffle(array) {
    var currentIndex = array.length, temporaryValue, randomIndex;

    // enquanto ainda tem elementos no array
    while (0 !== currentIndex) {

        // pega uma posicao randomica
        randomIndex = parseInt(Math.floor(Math.random() * currentIndex));
        currentIndex -= 1;

        // inverte a posicao randomica com a posicao atual do array
        temporaryValue = array[currentIndex];
        array[currentIndex] = array[randomIndex];
        array[randomIndex] = temporaryValue;
    }

    return array;
}