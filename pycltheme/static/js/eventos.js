let cityFilter = 'all';
let typeFilter = 'all';

function setYearOpen(toggle, open) {
    const eventsContainer = document.getElementById(toggle.id.slice(9));
    if (!eventsContainer) return;
    toggle.innerHTML = open ? '-' : '+';
    eventsContainer.style.display = open ? 'flex' : 'none';
}

function toggleYearEvents(target) {
    setYearOpen(target, target.innerHTML == '+');
}

// Abre todos los años cuando hay un filtro activo; si no, deja solo el año
// actual abierto (el que arranca con "-" en el template).
function syncYearVisibility() {
    const filtering = cityFilter !== 'all' || typeFilter !== 'all';
    const toggles = document.getElementsByClassName('etiqueta-eventos');
    for (const toggle of toggles) {
        if (filtering) {
            setYearOpen(toggle, true);
        } else {
            // año actual = el que tiene mayor valor numérico en su id
            setYearOpen(toggle, toggle.id === currentYearToggleId);
        }
    }
}

// Detecta el año más reciente para saber cuál dejar abierto al limpiar filtros.
const currentYearToggleId = (function () {
    let maxYear = -Infinity;
    let id = null;
    for (const toggle of document.getElementsByClassName('etiqueta-eventos')) {
        const year = parseInt(toggle.id.replace('etiqueta-eventos-', ''), 10);
        if (!isNaN(year) && year > maxYear) {
            maxYear = year;
            id = toggle.id;
        }
    }
    return id;
})();

function filter(){
    for (event of document.getElementById('past-events').getElementsByClassName('evento')){
        let showByCity = cityFilter == 'all' || event.dataset.city == cityFilter;
        let showByType = typeFilter == 'all' || event.dataset.type == typeFilter;
        event.style.display = showByCity && showByType ? 'block' : 'none';
    }
    syncYearVisibility();
    hideEmptyYears();
}

// Oculta el bloque de un año completo si no le quedan eventos visibles
// tras aplicar los filtros.
function hideEmptyYears() {
    for (const block of document.getElementsByClassName('year-block')) {
        const eventos = block.getElementsByClassName('evento');
        let visibles = 0;
        for (const ev of eventos) {
            if (ev.style.display !== 'none') visibles++;
        }
        block.style.display = visibles > 0 ? '' : 'none';
    }
}

function filterByCity(city){
    document.getElementById(`etiqueta-ciudad-${cityFilter}`).style.background = 'white';
    document.getElementById(`etiqueta-ciudad-${city}`).style.background = 'lightblue';
    cityFilter = city;
    filter();
}

function filterByType(type){
    document.getElementById(`etiqueta-tipo-${typeFilter}`).style.background = 'white';
    document.getElementById(`etiqueta-tipo-${type}`).style.background = 'lightblue';
    typeFilter = type;
    filter();
}
