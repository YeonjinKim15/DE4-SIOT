function makeChart(name, data, valueLabel) {
  const chart = am4core.create(name, am4charts.XYChart);
  chart.data = data.map(({ time, value }) => ({
    value,
    date: new Date(time * 1000)
  }));

  // Create axes
  var dateAxis = chart.xAxes.push(new am4charts.DateAxis());
  dateAxis.title.text = "Time";
  dateAxis.renderer.minGridDistance = 40;

  var valueAxis = chart.yAxes.push(new am4charts.ValueAxis());
  valueAxis.title.text = valueLabel;

  // Create series
  var series = chart.series.push(new am4charts.LineSeries());
  series.dataFields.valueY = "value";
  series.dataFields.dateX = "date";
  series.tooltipText = "{value}";

  series.tooltip.pointerOrientation = "vertical";

  chart.cursor = new am4charts.XYCursor();
  chart.cursor.snapToSeries = series;
  chart.cursor.xAxis = dateAxis;

  //chart.scrollbarY = new am4core.Scrollbar();
  chart.scrollbarX = new am4core.Scrollbar();
}

function initGraphs() {
  // Themes begin
  am4core.useTheme(am4themes_dark);
  am4core.useTheme(am4themes_animated);
  // Themes end

  const humidityChart = makeChart(
    "HumidityChart",
    window.chartData.temp,
    "Temp"
  );
  const tempChart = makeChart(
    "TempChart",
    window.chartData.humidity,
    "Humidity"
  );
  const lightChart = makeChart("LightChart", window.chartData.light, "Light");
}

am4core.ready(initGraphs);
