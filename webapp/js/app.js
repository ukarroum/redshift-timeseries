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

function update_chart(repeat = false)
{
    if($("#refresh").is(":checked") || !repeat)
    {
        $.post(
            "http://" + location.hostname + "/api/measures",
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

    if(repeat)
        setTimeout(update_chart, parseInt($("#refresh-rate").val()));
}

update_chart(true);

$("#refresh-now").on('click', function() { update_chart(false); });
$("#start-time").on('change', function() { update_chart(false); });
$("#window").on('change', function() { update_chart(false); });