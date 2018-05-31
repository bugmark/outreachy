let renderChart = function(chart_data) {
        
        let ctx = document.getElementById('canvas').getContext('2d');
        
        window.my_chart = new Chart(ctx, {
          type: 'bar',
          data: {
            labels: chart_data["cycles"],
            datasets: [
              {
                label: "Contracts",
                backgroundColor: getRandomColor(),
                data: data["contracts"]
              },
              
              {
                label: "Escrows",
                backgroundColor: getRandomColor(),
                data: data["escrows"]
              },
              
              {
                label: "Offers",
                backgroundColor: getRandomColor(),
                data: data["offers"]
              }
            ]
          },
          options: {
            responsive: true,
            legend: {
              position: 'top'
            },
            title: {
              display: true,
              text: 'Fast_buy bot data analysis for Number Of open offers, contracts and escrows per cycle.'
            }
          }
        });
      }
      
      let getRandomColor = function() {
        let letters = '0123456789ABCDEF'.split('')
        let color = '#'
        for (let i = 0; i < 6; i++) {
          color += letters[Math.floor(Math.random() * 16)]
        }
        return color
      }
      
    $(document).ready(function() {
      
      $.ajax({
        url: "https://gist.githubusercontent.com/snehasi/a17f7c1c726f1a06cf4ee3b9344bcba9/raw/d7fb88652dce02f96af5da7291477a3a965950cf/data.csv",
        async: false,
        success: function(csv) {
          data = {}
  
          for (let line of csv.split("\n"))
          {
            let arr = line.split(",");
            if (arr.length > 1)
            {
              data[arr[0]] = arr.slice(1).map(Number);
            }
          }
          
          renderChart(data);
        }
      });
    });