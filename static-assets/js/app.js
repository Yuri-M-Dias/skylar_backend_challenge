var CURRENT_URL = '';

$(document).ready(function () {
    $('#messageForm').submit(function (e) {
        var message = $('#messageInput').val();
        sendMessage(message);
        e.preventDefault();
    });

    pollMessages();
});

function displayMessage(data) {
    $('#chat').append(
        '<p>' +
        '<span><b>' + data['sender'] + ':</b></span>  ' +
        '<span>' + data['message'] + '</span>' +
        '</p>'
    );
    console.log(['displayMessage', data]);
}

function clearSendInput() {
    $('#messageInput').val('');
}

function sendMessage(message) {
    var data = {
        message: message
    };
    $.ajax({
        url: getCurrentURL() + '/publish',
        type: 'POST',
        dataType: 'json',
        data: data,
        success: function (data) {
            console.log(["Message sent to:", data]);
        },
        error: function (data) {
            console.error(["Error sending message:", data]);
        },
        complete: function () {
            clearSendInput();
        }
    });

}

function pollMessages() {
    var serverTimeout = 0;
    var self = this;

    $.ajax({
        url: getCurrentURL() + '/subscribe',
        dataType: 'json',
        success: function (data) {
            if(data !== null && data !== void 0){
                displayMessage(data);
            }
            self.serverTimeout = 0;
        },
        error: function (data) {
            self.serverTimeout = 5000;
        },
        complete: function () {
            setTimeout(pollMessages, self.serverTimeout);
        }
    });
}

function getCurrentURL() {
    return CURRENT_URL + '/redis';
}
