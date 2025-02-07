document.addEventListener('DOMContentLoaded', () => {
    const lightOff = document.getElementById('light-off');
    const lightOn = document.getElementById('light-on');
    const space = document.getElementById('space');
    const paragraph = document.getElementById('light-paragraph');

    lightOff.addEventListener('click', () =>{
        lightOff.classList.toggle('hidden');
        lightOn.classList.toggle('hidden');
        space.classList.replace('bg-gray','bg-deepestBlue');
        paragraph.classList.replace('text-lightBlue', 'text-deepestBlue');
    })

    lightOn.addEventListener('click', () =>{
        lightOn.classList.toggle('hidden');
        lightOff.classList.toggle('hidden');
        space.classList.replace('bg-deepestBlue', 'bg-gray');
        paragraph.classList.replace('text-deepestBlue', 'text-lightBlue');
    })
})