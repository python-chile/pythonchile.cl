// Paleta compartida entre gráficos, leyendas y cards de eventos.
// Los colores por tipo de evento coinciden con los definidos en cl.css.
const LABEL_COLORS = {
    // Tipos de evento
    'PyCon Chile': '#e22914',
    'PyDay': '#0057a8',
    'Meetup': '#4c9aff',
    'Hackaton': '#52c41a',
    // Sesiones
    'Charlas': '#0057a8',
    'Talleres': '#4c9aff',
    'Desafíos': '#52c41a',
    // Asistentes
    'asistentes': '#0057a8',
};

function colorForLabel(label) {
    return LABEL_COLORS[label] || '#ccc';
}

function plot(containerTag, data){
    const width = 300;
    const height = 200;
    const marginTop = 10;
    const marginRight = 16;
    const marginBottom = 20;
    const marginLeft = 32;

    const series = d3.stack()
      .keys(d3.union(data.map(d => d.label)))
      .value(([, D], key) => D.get(key).count)
    (d3.index(data, d => d.year, d => d.label));

    const x = d3.scaleBand()
      .domain(years)
      .range([marginLeft, width - marginRight])
      .padding(0.1);

    const y = d3.scaleLinear()
      .domain([0, d3.max(series, d => d3.max(d, d => d[1]))])
      .rangeRound([height - marginBottom, marginTop]);

    const keys = series.map(d => d.key);
    const color = d3.scaleOrdinal()
      .domain(keys)
      .range(keys.map(colorForLabel))
      .unknown("#ccc");

    const svg = d3.create("svg")
      .attr("width", width)
      .attr("height", height)
      .attr("viewBox", [0, 0, width, height])
      .attr("style", "max-width: 100%; height: auto;");

    svg.append("g")
    .selectAll()
    .data(series)
    .join("g")
      .attr("fill", d => color(d.key))
    .selectAll("rect")
    .data(D => D.map(d => (d.key = D.key, d)))
    .join("rect")
      .attr("x", d => x(d.data[0]))
      .attr("y", d => y(d[1]))
      .attr("height", d => y(d[0]) - y(d[1]))
      .attr("width", x.bandwidth())
    .append("title")
       .text(d => `${d.key}: ${d.data[1].get(d.key).count}`);

    svg.append("g")
      .attr("transform", `translate(0,${height - marginBottom})`)
      .call(d3.axisBottom(x).tickSizeOuter(0))
      .call(g => g.selectAll(".domain").remove());

    svg.append("g")
      .attr("transform", `translate(${marginLeft},0)`)
      .call(d3.axisLeft(y).ticks(null, "s"))
      .call(g => g.selectAll(".domain").remove());

    document.getElementById(`${containerTag}-chart`).append(svg.node());

    const legendContainer = document.getElementById(`${containerTag}-legend`);
    if (legendContainer) {
        legendContainer.innerHTML = '';
        legendContainer.classList.add('chart-legend');
        keys.forEach(key => {
            const item = document.createElement('span');
            item.className = 'chart-legend-item';
            const swatch = document.createElement('span');
            swatch.className = 'chart-legend-swatch';
            swatch.style.background = colorForLabel(key);
            const label = document.createElement('span');
            label.textContent = key;
            item.append(swatch, label);
            legendContainer.append(item);
        });
    }
}
plot('events-count', eventsCounts);
plot('sessions-count', sessionsCounts);
plot('attendees-count', attendeesCounts);
