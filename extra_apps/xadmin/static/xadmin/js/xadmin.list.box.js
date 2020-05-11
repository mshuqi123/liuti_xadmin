
;function click_action_info(id){
    var x=id
    $.get("/box_request/get_boxapitime/",
                {
                    id: x,
                },
                function (result) {
                    alert(result.message);
                });
    }
;function click_memory_info(filename){
    var x=filename
    $.get("/data_handle/memory",
                {
                    filename: x,
                },
                function (result) {
                    alert(result.message);
                });
    }
;function click_cpu_info(filename){
    var x=filename
    $.get("/data_handle/cpu",
                {
                    filename: x,
                },
                function (result) {
                    alert(result.message);
                });
    }