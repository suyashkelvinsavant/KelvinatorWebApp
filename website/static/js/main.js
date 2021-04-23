function updateList() {
    fetch("./tradeList").then(response => response.json()).then(tradeList => {
        fetch("./tradeHistory").then(response => response.json()).then(tradeHistory => {
            document.getElementById("tbody").innerHTML="";
            tradeList=tradeList.concat(tradeHistory);
            for (i in tradeList) {
                var tr = document.createElement("tr");
                var th = document.createElement("th")
                var td1 = document.createElement("td")
                var td2 = document.createElement("td")
                var td3 = document.createElement("td")
                var td4 = document.createElement("td")
                var td5 = document.createElement("td")
                var td6 = document.createElement("td")
                var td7 = document.createElement("td")
                th.setAttribute("scope", "row")
                th.innerText = tradeList[i][0]
                td1.innerText = tradeList[i][1]
                td2.innerText = tradeList[i][2]
                td3.innerText = tradeList[i][3]
                td4.innerText = tradeList[i][4]
                td5.innerText = tradeList[i][5]
                td6.innerText = tradeList[i][6]
                td7.innerText = tradeList[i][7]
                tr.appendChild(th)
                tr.appendChild(td1)
                tr.appendChild(td2)
                tr.appendChild(td3)
                tr.appendChild(td4)
                tr.appendChild(td5)
                tr.appendChild(td6)
                tr.appendChild(td7)
                if (tradeList[i][6] > 0) {
                    tr.classList.add("table-success");
                } else if (tradeList[i][6] < 0) {
                    tr.classList.add("table-danger");
                }
                var tbody = document.getElementById("tbody")
                tbody.appendChild(tr)
            }
        })
    })
}
setInterval(updateList, 10000)






// fetch("./stockList").then(response => response.json()).then(stockList => {
//     for (i in stockList) {
//         var tag = document.createElement('option');
//         var text = document.innerHTML(`${stockList[i].substring(0, stockList[i].length - 3)}`);
//         tag.appendChild(text);
//         var element = document.getElementById('stockSelector');
//         tag.setAttribute('value', `${stockList[i]}`);
//         if (i == 0) {
//             tag.setAttribute('selected', '')
//         }
//         element.appendChild(tag);
//     }
//     var e = document.getElementById("stockSelector");
//     var symbol = e.value;
//     highChart(symbol);
// });
// function highChart(symbol) {
//     Highcharts.getJSON(`./indicator/${symbol}`, data => {
//         //Highcharts.getJSON(`../json/signal/${symbol}.json`, signalData => {
//         fetch(`./signal/${symbol}`).then(response => response.json()).then(flagData => {

//             var stockData = [],
//                 rsiData = [],
//                 emaData = [],
//                 wmaData = [],
//                 ema200Data = [],
//                 areaRangeData = [],
//                 dataLength = data.length,
//                 i = 0;
//             for (i; i < dataLength; i += 1) {
//                 stockData.push([
//                     data[i][0], // the date
//                     data[i][1] // close
//                 ]);
//                 ema200Data.push([
//                     data[i][0], // the date
//                     data[i][5] // close
//                 ]);

//                 rsiData.push([
//                     data[i][0], // the date
//                     data[i][2], // the rsi
//                 ]);
//                 emaData.push([
//                     data[i][0], // the date
//                     data[i][3], // the ema
//                 ]);
//                 wmaData.push([
//                     data[i][0], // the date
//                     data[i][4], // the wma
//                 ]);
//                 areaRangeData.push([
//                     data[i][0], // the date
//                     data[i][3], // the ema
//                     data[i][4], // the wma
//                 ]);
//             }
//             const chart = Highcharts.stockChart('container', {
//                 chart: {
//                     height: 1000
//                 },

//                 title: {
//                     text: `${symbol.substring(0, symbol.length - 3)} Stock Chart`
//                 },

//                 subtitle: {
//                     text: 'Kelvinator Trading'
//                 },

//                 rangeSelector: {
//                     selected: 2
//                 },
//                 yAxis: [{

//                     height: '70%',
//                     resize: {
//                         enabled: true
//                     },
//                 }, {
//                     plotLines: [{
//                         value: 50,
//                         color: 'black',
//                         width: 2,
//                     }],
//                     top: '70%',
//                     height: '30%',
//                     offset: 0,
//                 }],

//                 series: [{
//                     name: `${symbol} Stock Price`,
//                     data: stockData,
//                     id: 'stockChart',
//                     type: 'line',
//                     threshold: null,
//                     tooltip: {
//                         valueDecimals: 2
//                     },
//                 }, {
//                     name: `${symbol} Stock Price`,
//                     data: ema200Data,
//                     linkedto: 'stockChart',
//                     type: 'line',
//                     threshold: null,
//                     tooltip: {
//                         valueDecimals: 2
//                     },
//                 },
//                 {
//                     type: 'line',
//                     id: 'rsi',
//                     name: 'RSI',
//                     data: rsiData,
//                     color: 'blue',
//                     yAxis: 1,
//                     tooltip: {
//                         valueDecimals: 2
//                     },
//                 },
//                 {
//                     type: 'line',
//                     linkedto: 'rsi',
//                     name: 'EMA',
//                     color: 'green',
//                     data: emaData,
//                     yAxis: 1,
//                     tooltip: {
//                         valueDecimals: 2
//                     },
//                 },
//                 {
//                     type: 'line',
//                     linkedto: 'rsi',
//                     name: 'WMA',
//                     id:'WMA',
//                     data: wmaData,
//                     color: 'red',
//                     yAxis: 1,
//                     tooltip: {
//                         valueDecimals: 2
//                     }
//                 },
//                     {
//                         type: 'flags',
//                         data: flagData,
//                         yAxis:0,
//                         onSeries: 'stockChart',//'WMA',//'stockChart',
//                         shape: 'squarepin',
//                     }
//                     // {
//                     //     type:'arearange',
//                     //     linkedto:'rsi',
//                     //     name: 'EMA & WMA',
//                     //     data: areaRangeData,
//                     //     yAxis: 1,
//                     //     tooltip: {
//                     //         valueDecimals: 2
//                     //     },
//                     // },
//                 ],

//                 responsive: {
//                     rules: [{
//                         condition: {
//                             maxWidth: 500
//                         },
//                         chartOptions: {
//                             chart: {
//                                 height: 300
//                             },
//                             subtitle: {
//                                 text: null
//                             },
//                             navigator: {
//                                 enabled: false
//                             }
//                         }
//                     }]
//                 }
//             });

//             document.getElementById('small').addEventListener('click', () => {
//                 chart.setSize(400);
//             });

//             document.getElementById('large').addEventListener('click', () => {
//                 chart.setSize(800);
//             });

//             document.getElementById('auto').addEventListener('click', () => {
//                 chart.setSize(null);
//             });
//         });
//     });
// }

// function updateChart() {
//     var e = document.getElementById("stockSelector");
//     var symbol = e.value;
//     highChart(symbol);
// }