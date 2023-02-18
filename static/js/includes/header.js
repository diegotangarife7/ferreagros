(function(){
    const openButton = document.querySelector('.nav__menu')
    const menu = document.querySelector('.header')

    openButton.addEventListener('click', ()=>{
        menu.classList.toggle('nav__link--show')
    })

})()