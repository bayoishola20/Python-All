let margin = {
    top: 20,
    right: 10,
    bottom: 20,
    left: 10
};


let w = 1000 - margin.left - margin.right;
let h = 600 - margin.bottom - margin.top;


let svg = d3.select("#map")
            .append("svg")
            .attr("width", w + margin.left + margin.right)
            .attr("height", h + margin.top + margin.bottom)
            .append("g")
            .attr("transform", "translate(" + margin.left + "," + margin.top + ")");


let slider = d3.select("#mySlider").node();
let test = noUiSlider.create(slider, {
    start: [20, 80],
    connect: true,
    orientation: "horizontal",
    //tooltips: [true, true],
    behaviour: "drap-snap",
    range: {
        'min': 0,
        'max': 100
    },
});

function toFormat(v) {
    var tt = new Date(v);
    return "Date:" + tt.getDate() + "." + (tt.getMonth() + 1) + "."
    + tt.getFullYear() + " Time:" + tt.getHours() + ":" + tt.getMinutes() + ":"
    + tt.getSeconds();
}

let proj = d3.geoEqualEarth();
// .translate([w / 2, h / 2]) <= can be avoided using .fitExtent()
// .center([11.57549, 48.13743])
// .scale(100000);

let path = d3.geoPath()
            .projection(proj);


let data;

Promise.all([
    d3.json("./munich_25_boroughs.geojson"),
    d3.json("./tweet_201709_16_22.geojson"),
    ]).then(function(files) {
    data = files[1].features;
    //console.log(data.length);
    proj.fitExtent([
        [0, 0],
        [w, h]
        ], files[0]);

        let minDate = d3.min(data, d => d.properties.utcms);
        let maxDate = d3.max(data, d => d.properties.utcms);
        
        // console.log(minDate, maxDate);
        
        slider.noUiSlider.updateOptions({
            range: {
            'min': d3.min(data, d => d.properties.utcms),
            'max': d3.max(data, d => d.properties.utcms)
            },
            start: [
            minDate,
            maxDate
            ]
        });
        let map = svg.append("g")
                    .attr("id", "countries")
                    .selectAll("path")
                    .data(files[0].features)
                    .enter()
                    .append("path")
                    .attr("d", path)
                    .style("fill", "#ccd9ff")
                    .style("stroke", "#fcfcfc")
                    .style("stroke-width", "0.8");
            
        let circles = svg.append("g")
                        .attr("id", "eq")
                        .selectAll("circle")
                        .data(files[1].features)
                        .enter()
                        .append("circle")
                        .attr("cx", d => proj([d.geometry.coordinates[0], d.geometry.coordinates[1]])[0])
                        .attr("cy", d => proj([d.geometry.coordinates[0], d.geometry.coordinates[1]])[1])
                        .attr("r", 7)
                        .style("fill", "green")
                        .style("opacity", "0.5")
        
        let dateValues = [d3.select("#startEvent").node(),d3.select("#endEvent").node()];
        //console.log(dateValues);

        slider.noUiSlider.on("update", function(values, handle, c, d, e){
        let time = [Math.round(+values[0]), Math.round(+values[1])];

        let test = circles //svg.selectAll("circle")
        .style("fill", "white")
        .style("opacity", 0) //not visible
        .filter(function(d) {
        return d.properties.utcms <= time[1] && d.properties.utcms >= time[0];
        })
        .style("fill", "green")
        .style("opacity", 0.5);

        dateValues[handle].innerHTML = "Date: " + getCurrentDate(new
            Date(time[handle])) + " Time: " + getCurrentTime(new Date(time[handle]));
            });
    });