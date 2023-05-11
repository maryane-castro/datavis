/* globals Chart:false, feather:false */

(() => {
  'use strict'

  feather.replace({ 'aria-hidden': 'true' })

  // Graphs
  const ctx = document.getElementById('myChart')
  // eslint-disable-next-line no-unused-vars

  const myChart = new Chart(ctx, {
    type: 'line', //line
    data: {
      labels: nm,

      datasets: [{
        data: dt,
        lineTension: 0,
        backgroundColor: '#fff',
        borderColor: '#007bff',
        borderWidth: 3,
        pointBackgroundColor: '#007bff'
      }]
    },
    options: {
      plugins: {
        legend: {
          display: false
        },
        tooltip: {
          boxPadding: 3
        }
      }
    }
  })
})()


