(function () {
    const burger = document.querySelector('.burger_menu');
    const main_menu = document.querySelector('.top__main');
    burger.addEventListener('click', () => {
        burger.classList.toggle('burger_close');
        main_menu.classList.toggle('vision');
    });
}());