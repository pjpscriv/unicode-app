// Listeners
function listeners() {

    // When a Text Field gets new input...
    $("input[type=text]").on("input", function() {
        update_fields(this);
    });

    // Number Format Switch
    $("input[type=checkbox]").on("input", function() {
        // TODO: Maybe convert shit here?
        var convert_to_hex = $("input[type=checkbox]").is(":checked");
        var value = $("input.number").val();
        // Reformat input just to be safe
        value = number_format(value, !convert_to_hex);


        // Convert
        var numbers = "";
        if (convert_to_hex) {
            numbers = dec_to_hex(value);
        } else {
            numbers = hex_to_dec(value);
        }

        $("input.number").val(numbers);

        //update_fields($("input.number"));
    });
}



// Input Cleaners
function number_format(value, u_format) {
    if (u_format) {
        var units = value.split(",");
        for (var i in units) {
            console.log("Thing; "+i+", "+units[i]);
        }

        //value.replace();

        return value;
    } else {
        value = value.replace(/([^0-9|^,])/ig, '');
        value = value.replace(/^,/ig, '');
        value = value.replace(/,,/ig, ',');
        return value;
    }
}
function binary_format(value) {
  return value.replace(/[^0|^1|^,]/g, '');
}



// AJAX 
function update_fields(updated_field) {
    
    // Get the relevant data
    var field = $(updated_field).attr("name");
    var value = $(updated_field).val();
    var num_f = $("input[type=checkbox]").is(":checked");

    // Clear Invalid Input
    if (field === "number") {
      value = number_format(value, num_f);
      $("input.number").val(value);
    } else if (field == "binary") {
      value = binary_format(value);
      $("input.binary").val(value);
    }

    console.log("\""+field+"\": \""+value+"\" (fmt: \""+num_f+"\")");
    if (field == null || value == null || num_f == null) {
        console.log("Cannot send values. At least one is NULL.");

    // THIS IS A HACK
    } else if (field == "number" && value.endsWith(",")) {
        console.log('Number in unconvertable format atm.')



    } else {

        // Send AJAX
        $.ajax({
        url: '/convert/',
        data: {
          'field': field,
          'value': value,
          'num_format': num_f
        },
        dataType: 'json',
        // Receive Data
        success: function (data) {

              console.log("Data Recieved:");
              console.log(data);

              // Put Data Onto Page
              $("input.letter").val(data.letter);
              $("input.number").val(data.number);
              $("input.binary").val(data.binary);
            }
        });
    }
}

$(document).ready(listeners());