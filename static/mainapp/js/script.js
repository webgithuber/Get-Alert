
      
     document.getElementById ("select_state").addEventListener ("click", states);
     document.getElementById ("select_district").addEventListener ("click", district);
     document.getElementById ("pin").addEventListener ("click", time);
     function states(hello) {
       
        var list = document.getElementById("select_district");
        while (list.childElementCount > 1) {
          list.removeChild(list.lastChild);
        }
        var st_list = document.getElementById("select_state").childElementCount;

        if (st_list == 1) {
          fetch("https://cdn-api.co-vin.in/api/v2/admin/location/states")
            .then(function (response) {
              return response.json();
            })
            .then(function (datas) {
              for (var i = 0; i < datas["states"].length; i++) {
                var para = document.createElement("OPTION");
                para.value = datas["states"][i]["state_id"];
                para.innerHTML = datas["states"][i]["state_name"];
                document.getElementById("select_state").appendChild(para);
              }
            });
        }
      }
      function district() {
        var s_id = document.getElementById("select_state").value;
        var url =
          "https://cdn-api.co-vin.in/api/v2/admin/location/districts/" + s_id;

        fetch(url)
          .then(function (response) {
            return response.json();
          })
          .then(function (datas) {
            for (var i = 0; i < datas["districts"].length; i++) {
              var para = document.createElement("OPTION");
              para.value = datas["districts"][i]["district_id"];
              para.innerHTML = datas["districts"][i]["district_name"];
              document.getElementById("select_district").appendChild(para);
            }
          });
      }

      function time()
      {
        var list = document.getElementById("select_district");
        while (list.childElementCount > 1) {
          list.removeChild(list.lastChild);
        }
        var list = document.getElementById("select_state");
        while (list.childElementCount > 1) {
          list.removeChild(list.lastChild);
        }

        var z=document.getElementById('date');

            const d = new Date();
        var mnth= d.getMonth()+1;
        if(mnth<10){mnth="0"+mnth;}
        else{ mnth = mnth.toString();}
        var dt=d.getDate();
        if(dt<10){dt="0"+dt;}
        else{ dt = dt.toString();}
        var year=d.getFullYear();
        year = year.toString();
        var today=dt + '-' + mnth + '-' + year;
        
        z.value=today;
      }