const ctx = document.getElementById('myChart');

chart = new Chart(ctx, {
type: 'line',
data: {
  labels: [],
  datasets: [{
    label: 'Measures',
    data: [],
    borderWidth: 1
  }]
},
options: {
  scales: {
    y: {
      beginAtZero: true
    }
  }
}
});

function update_chart()
{
    $.ajax({
      url: "http://127.0.0.1:5000/api/measures",
      async: true,
      dataType: 'json',
      type: "get",
    }).done(function (data) {
        chart.data.labels = data.labels;
        chart.data.datasets[0].data = data.data;
        chart.update();
    });

    setTimeout(update_chart, 2 * 1000);
}

update_chart();

