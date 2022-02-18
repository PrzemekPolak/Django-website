function parse_it(data) {
    return JSON.parse(document.getElementById(data).textContent);
}

// wczytaj dane do js
const chart_time_data = parse_it('chart_time_data');
const chart_price_data = parse_it('chart_price_data');
const chart_id_data = parse_it('chart_id_data');
    
const data = {
    labels: chart_time_data,
    datasets: [{
        label: chart_id_data,
        backgroundColor: 'rgb(235, 233, 230)',
        borderColor: 'rgb(255, 99, 132)',
        data: chart_price_data,
    }]
};
    
const config = {
    type: 'line',
    data: data,
    options: {
        plugins: {
            legend: {
            // kolor i rozmiar napisu BTC
                labels: {
                    color: "white",
                    font: {
                        size: 20
                        }
                }
            }
        },
        // opisy osi x i y
        scales: {
            y: {
                ticks: {
                    color: "white",
                    font: {
                        size: 14,
                    },
                }
            },
            x: {
                ticks: {
                    color: "white",
                    font: {
                        size: 14,
                    },
                }
            }
        },
    

    }
};
  
const myChart = new Chart(
    document.getElementById('myChart'),
    config
);