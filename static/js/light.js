document.addEventListener('DOMContentLoaded', () => {
    const lightOff = document.getElementById('light-off');
    const lightOn = document.getElementById('light-on');
    const space = document.getElementById('space');
    const paragraph = document.getElementById('light-paragraph');
    const paragraphTwo = document.getElementById('light-paragraph-2')

    lightOff.addEventListener('click', () =>{
        lightOff.classList.toggle('hidden');
        lightOn.classList.toggle('hidden');
        space.classList.replace('bg-gray','bg-deepestBlue');
        paragraph.classList.toggle('hidden');
        paragraphTwo.classList.toggle('hidden');
    })

    lightOn.addEventListener('click', () =>{
        lightOn.classList.toggle('hidden');
        lightOff.classList.toggle('hidden');
        space.classList.replace('bg-deepestBlue', 'bg-gray');
        paragraph.classList.toggle('hidden');
        paragraphTwo.classList.toggle('hidden');
        
    })
})