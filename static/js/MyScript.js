$(document).ready(function () {



    $("p").click(function () {
        $(this).hide();
    });

    DesignTable();

    

    $("#demo").click(function () { myFunction();}    );

    $("#insertnumbers").click(function () { insertnumbers(); });


    

    $("#checkTable").click(function () {

        

        var chek_tab_bol = checkTable();

        
        
        if (chek_tab_bol) {

            win = false;

            Constant_Input();
            alert("good- start solving");
           // debugger

            setTimeout(SolveSudoku, 300);

            SolveSudoku(1);
         //   alert("win");
        }
        else {          
            alert("check input");
        }

    });



    $("#t1").click(function () {
        

    },

        function () {
            alert("Bye! You now enter table1!");
            $(this).css("background-color", "red");
            $("#i1").css("background-color", "red");

        });

 
});


function myFunction() {
    document.getElementById('demo').innerHTML = Date();
};

function insertnumbers() {
    /*
    var place=[1,6,9,12,18,23,26,27,31,33,36,37,38,41,44,45,46,49,51,55,56,59,64,70,73,76,81];
    var value = [2, 1, 7, 4, 8, 7, 3, 5, 2, 7, 9, 1, 7, 9, 5, 4, 8, 4, 5, 3, 8, 2, 4, 7, 6, 8, 1];

    //debugger
    for (var i = 0; i < place.length; i++) {
        var num= place[i]
        document.getElementById('i3' + num).value = value[i];
    }

    */
    var place = [1,2,6,11,12,13,17,19,26,32,36,39,41,43,46,50,56,63,65,69,70,71,76,80,81];
    var value = [9,4,7,1,8,5,4,6,3,1,9,9,3,8,2,8,9,2,2,4,1,9,1,6,3];

    //debugger
    for (var i = 0; i < place.length; i++) {
        var num = place[i]
        document.getElementById('i3' + num).value = value[i];
    }


}


function prepareTable() {
    document.getElementById('i13').innerHTML = 1;
}



// make lines in the table
function DesignTable() {

    for (var i = 3; i < 7; i = i +3) { 
        for (var x = 0; x < 81; x = x + 9) {
            var num = i + x;
            $("#td3" + num).css("border-right", "2px solid black");
        }
        
    }

    $("#tr3" + 3).css("border-bottom", "2px solid black");
    $("#tr3" + 6).css("border-bottom", "2px solid black");
    $("#tr3" + 9).css("border-bottom", "2px solid black");
}


// make sure inserting only numbers
function Constant_Input() {
    for (var i = 0; i < 82; i++) {

        var element = document.getElementById('i3'+i);
        if (!(element != null && element.value == '')) {
            $("#i3" + i).css("background-color", "DarkGray ");
            // document.getElementById("#i3" + i).readOnly = true;
            // document.getElementById("#i3" + i).setAttribute("readonly", true);
            $("#i3" + i).prop('readonly', true);
        }
    }
}


// make just 1-9 as good input
    function Check_Input(selectObject) {
        var value = selectObject.value;
        if (!(value > 0 && value < 10)) {
            selectObject.value = '';
        }
    }




    // clean table from data
    function CleanTable() {
        debugger
        
        for (var i = 1; i < 82; i++) {

            var element = document.getElementById('i3' + i);

            $("#i3" + i).css("background-color", "coral");
            // document.getElementById("#i3" + i).readOnly = true;
            // document.getElementById("#i3" + i).setAttribute("readonly", true);
            $("#i3" + i).prop('readonly', false);
            document.getElementById('i3' + i) = '';
        }
        
    }



