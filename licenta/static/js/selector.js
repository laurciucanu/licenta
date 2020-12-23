document.getElementById('resizing_select').addEventListener(
     'change',
     function() { 
       var resize = document.getElementById("resizing_select");        
       var hidden_opt = document.getElementById("width_tmp_option");
       hidden_opt.innerHTML = resize.options[resize.selectedIndex].textContent;
       var hidden_sel = document.getElementById("width_tmp_select");
       hidden_sel.style.display = "initial";
       resize.style.width = hidden_sel.clientWidth + "px";
       hidden_sel.style.display = "none";
       },
     false
  );
  