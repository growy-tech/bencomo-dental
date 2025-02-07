document.addEventListener('DOMContentLoaded', () => {
    const menu = document.getElementById('menu');
    const close = document.getElementById('close-icon');
    const open = document.getElementById('open-icon');

    close.addEventListener('click', () => {
        menu.classList.toggle('-translate-x-full')
        open.classList.toggle('hidden');
        if(menu.classList.contains('hidden')){

        }else{
            menu.classList.contains('hidden');
        }
    })

    open.addEventListener('click', () => {
        menu.classList.toggle('-translate-x-full')
        open.classList.toggle('hidden');
    })


})