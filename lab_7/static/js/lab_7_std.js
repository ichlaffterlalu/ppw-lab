var addFriend = function(nama, npm) {
    $.ajax({
        method: "POST",
        url: "{% url "lab-7:add-friend" %}",
        data: { name: nama, npm: npm},
        success : function (friend) {
            html = '<a class="list-group-item clearfix">' +
                friend.friend_name +
                '</a>';
            $("#friend-list").append(html)
        },
        error : function (error) {
            alert("Mahasiswa tersebut sudah ditambahkan sebagai teman")
        }
    });
};

$("#add-friend").on("submit", function () {
name = $("#field_name").val()
npm = $("#field_npm").val()
    addFriend(name, npm)
    event.preventDefault();
});

$("#field_npm").change(function () {
    console.log( $(this).val() );
    npm = $(this).val();
    $.ajax({
        method: "POST",
        url: '{% url "lab-7:validate-npm" %}',
        data: {
            'npm': npm
        },
        dataType: 'json',
        success: function (data) {
            console.log(data)
            if (data.is_taken) {
                alert("Mahasiswa dengan npm seperti ini sudah ada");
            }
        }
    });
});