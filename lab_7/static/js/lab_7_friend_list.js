$( document ).ready(function () {
    {// lengkapi pemanggilan ajax berikut untuk mengambil daftar teman yang ada di database #}
    $.ajax({
        method: "GET",
        url: "", //URL untuk mendapatkan list teman]
        success: function (response) {
            //tampilkan list teman ke halaman
            //hint : gunakan fungsi jquery append()
        },
        error: function(error){
            //tampilkan pesan error
        }
    });
});