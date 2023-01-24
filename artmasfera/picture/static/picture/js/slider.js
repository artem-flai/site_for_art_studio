let offset = 0;
const images = document.getElementsByClassName('mk__foto').length
const sliderLine = document.querySelector('.content__mk__line');

document.querySelector('.slider-next').addEventListener('click', function (){
    offset = offset + 600;
    if (offset >= images * 600) {
        offset = 0;
    }
    sliderLine.style.left = -offset + 'px';
});

document.querySelector('.slider-prev').addEventListener('click', function (){
    offset = offset - 600;
    if (offset < 0) {
        offset = (images - 1) * 600;
    }
    sliderLine.style.left = -offset + 'px';
});