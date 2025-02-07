window.addEventListener('scroll', () => {
    const secciones = document.querySelectorAll('section');

    secciones.forEach(seccion => {
        const alturaVentana = window.innerHeight;
        const distanciaAlTop = seccion.getBoundingClientRect().top;

      if (distanciaAlTop < alturaVentana * 0.75) { // Ajusta 0.75 para controlar el punto de activación
        seccion.classList.remove('opacity-0');
        seccion.classList.add('opacity-100');
        } else {
            seccion.classList.remove('opacity-100');
            seccion.classList.add('opacity-0');
            }
        });
    });