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
    if($("#refresh").is(":checked"))
    {
        $.post(
            "http://127.0.0.1:5000/api/measures",
            {
                starttime: $("#start-time").val(),
                window: $("#window").val()
            },
            function (data) {
            chart.data.labels = data.labels;
            chart.data.datasets[0].data = data.data;
            chart.update();
        });
    }

    setTimeout(update_chart, parseInt($("#refresh-rate").val()));
}

update_chart();

$("#start-time").on('change', update_chart);
$("#window").on('change', update_chart);