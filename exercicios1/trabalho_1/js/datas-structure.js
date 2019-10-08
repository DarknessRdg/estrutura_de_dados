'use strict';

const IMAGE_PATH = './assets/game-images/';
class Cell {
    constructor(image) {
        this.image = image;
        this.imagePath = IMAGE_PATH + image + '.jpg';
        this.next = null;
    }
}


class Lista {
    constructor() {
        this.cabeca = new Cell(undefined);
        this.length = 0;
        this.ultimo = this.cabeca;
    }

    get(index) {
        let aux = this.cabeca;

        if (index >= this.length)
            aux = null;
        else {
            for (let i = 0; i <= index; i++) {
                aux = aux.next;
            }
        }

        return aux;
    }

    remove(index) {
        let anterior = this.cabeca;

        for(let i = 0; i < index; i++) {
            anterior = anterior.next;
        }

        let morta = anterior.next;

        if (morta !== null) {
            anterior.next = morta.next;
            this.length --;
        }
        return morta;
    }

    add(image) {
        const newCell = new Cell(image);

        this.ultimo.next = newCell;
        this.ultimo = newCell;
        this.length ++;
    }

    cellAt(index) {
        let aux = this.cabeca.next;
        for (let i = 0; i < index; i++)
            aux = aux.next;

        return aux;
    }

    show() {
        let aux = this.cabeca.next;
        while(aux !== null) {
            console.log(aux.image);
            aux = aux.next
        }
    }
}