let margin = {
    top: 20,
    right: 10,
    bottom: 20,
    left: 10
};

let slider = d3.select("#mySlider").node();
let test = noUiSlider.create(slider, {
    start: [20, 80],
    connect: true,
    orientation: "horizontal",
    tooltips: [true, true],
    behaviour: "drap-snap",
    range: {
        'min': 0,
        'max': 100
    },
}