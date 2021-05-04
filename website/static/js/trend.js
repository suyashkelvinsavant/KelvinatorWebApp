function updateList() {
    fetch("./trenddata").then(response => response.json()).then(tradeList => {
        document.getElementById("tbody").innerHTML = "";
        for (i in tradeList) {
            var tr = document.createElement("tr");
            var th = document.createElement("th")
            var td1 = document.createElement("td")
            var td2 = document.createElement("td")
            var td3 = document.createElement("td")
            th.setAttribute("scope", "row")
            th.innerText = tradeList[i][0]
            td1.innerText = tradeList[i][1]
            td2.innerText = tradeList[i][2]
            td3.innerText = tradeList[i][3]
            tr.appendChild(th)
            tr.appendChild(td1)
            tr.appendChild(td2)
            tr.appendChild(td3)
            if (tradeList[i][0] =="BUY") {
                tr.classList.add("table-success");
            } else if (tradeList[i][0] =="SELL") {
                tr.classList.add("table-danger");
            }
            var tbody = document.getElementById("tbody")
            tbody.appendChild(tr)
        }
    })

}
setInterval(updateList, 10000)

