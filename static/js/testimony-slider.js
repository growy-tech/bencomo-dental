document.addEventListener('DOMContentLoaded', () => {
    const testimonyOne = document.getElementById('testimony-1');
    const testimonyTwo = document.getElementById('testimony-2');
    const testimonyThree = document.getElementById('testimony-3');
    const testimonyFour = document.getElementById('testimony-4');
    const arrowLeft = document.getElementById('arrow-left');
    const arrowRight = document.getElementById('arrow-right');
    const testimonyImageOne = document.getElementById('testimony-image-1');
    const testimonyImageTwo = document.getElementById('testimony-image-2');
    const testimonyImageThree = document.getElementById('testimony-image-3');
    const arrowLeftTestimony = document.getElementById('testimony-image-arrow-left');
    const arrowRightTestimony = document.getElementById('testimony-image-arrow-right');
    
    
    const packs = [testimonyOne, testimonyTwo, testimonyThree, testimonyFour];
    const images = [testimonyImageOne, testimonyImageTwo, testimonyImageThree];

    let actual = 0;
    let actualImg = 0;

    function showNext(){
        actual = (actual + 1) % packs.length;
        showPack(actual);
    }

    function showLast(){
        actual = (actual - 1 + packs.length) % packs.length;
        showPack(actual)
    }

    function showPack(indice){
        packs.forEach((pack, i) => {
            pack.style.display = i === indice ? 'block' : 'none';
        });
    }

    function showNextImage(){
        actualImg = (actualImg + 1) % images.length;
        showImage(actualImg);
    }

    function showLastImage(){
        actualImg = (actualImg - 1 + images.length) % images.length;
        showImage(actualImg);
    }

    function showImage(index){
        images.forEach((image, i) => {
            image.style.display = i === index ? 'block' : 'none';
        })
    }

    showPack(actual);
    showImage(actualImg);

    arrowLeftTestimony.addEventListener('click', showLastImage);
    arrowRightTestimony.addEventListener('click', showNextImage);
    arrowLeft.addEventListener('click', showLast);
    arrowRight.addEventListener('click', showNext)


})