let cityFilter = 'all';
let typeFilter = 'all';

function toggleYearEvents(target) {
    const eventsContainer = document.getElementById(target.id.slice(9));
    if(target.innerHTML == '-') {
        target.innerHTML = '+';
        eventsContainer.style.display = 'none';
    } else {
        target.innerHTML = '-';
        eventsContainer.style.display = 'flex';
    }
}
function filter(){
    for (event of document.getElementById('past-events').getElementsByClassName('evento')){
        let showByCity = cityFilter == 'all' || event.dataset.city == cityFilter;
        let showByType = typeFilter == 'all' || event.dataset.type == typeFilter;
        event.style.display = showByCity && showByType ? 'block' : 'none';
    }
}

function filterByCity(city){
    console.log(`etiqueta-city-${cityFilter}`)
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
