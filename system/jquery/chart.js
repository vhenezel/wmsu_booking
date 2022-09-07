document.addEventListener("DOMContentLoaded", function () {
    // Bar Chart
    var barChartData = {
       labels: ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30"],
       datasets: [{
          label: 'served',
          backgroundColor: 'rgb(79,129,189)',
          borderColor: 'rgba(0, 158, 251, 1)',
          borderWidth: 1,
          data: [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60]
       }]
    };
 
   var ctx = document.getElementById('bargraph').getContext('2d');
   window.myBar = new Chart(ctx, {
      type: 'bar',
      data: barChartData,
      options: {
         responsive: true,
         legend: {
            display: false,
         }
      }
   });
});