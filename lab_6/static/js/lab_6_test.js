$( document ).ready(function() {
    var button_8 = $('button:contains("8")');
    var button_4 = $('button:contains("4")');
    var button_0 = $('button:contains("0")');
    var button_9 = $('button:contains("9")');
    var button_1 = $('button:contains("1")');
    var button_5 = $('button:contains("5")');
    var button_add = $('button:contains("+")');
    var button_sub = $('button:contains("-")');
    var button_mul = $('button:contains("*")');
    var button_div = $('button:contains("/")');
    var button_sin = $('button:contains("sin")');
    var button_tan = $('button:contains("tan")');
    var button_log = $('button:contains("log")');
    var button_clear = $('button:contains("AC")');
    var button_res = $('button:contains("=")');
    var textArea = $(".chat-text");

    QUnit.test("Enter Button on Chat Box Test", function( assert ){
      $(".chat-textarea").val("I went to the market.");
      $(".chat-button").click();
      assert.equal($('.msg-insert').html().trim().includes("<p class=\"msg-send\">I went to the market.</p>"), true, "Input test message must be successful.");
    });

    QUnit.test("<Return> Keypress on Chat Box Test", function( assert ){
      $(".chat-textarea").val("I went to the market, again.");
      var press = jQuery.Event("keypress");
      press.which = 13;
      $(".chat-textarea").trigger(press);
      assert.equal($('.msg-insert').html().trim().includes("<p class=\"msg-send\">I went to the market.</p>"), true, "Input test message must be successful.");
    });

    QUnit.test("Log Button on Calculator Test", function( assert ){
      button_1.click();
      button_0.click();
      button_0.click();
      button_0.click();
      button_log.click();
      assert.equal( $('#print').val(), 3.0, "log(1000) must be 3.0" );
      button_clear.click();
    });

    QUnit.test("Sin Button on Calculator Test", function( assert ){
      button_9.click();
      button_0.click();
      button_sin.click();
      assert.equal( $('#print').val(), 1.0, "sin(90) must be 1.0" );
      button_clear.click();
    });

    QUnit.test("Tan Button on Calculator Test", function( assert ){
      button_4.click();
      button_5.click();
      button_tan.click();
      assert.equal( $('#print').val(), 1.0, "tan(45) must be 1.0" );
      button_clear.click();
    });

    QUnit.test("Addition on Calculator Test", function( assert ) {
      button_8.click();
      button_add.click();
      button_4.click();
      button_res.click();
      assert.equal( $('#print').val(), 12, "8 + 4 must be 12" );
      button_clear.click();
    });

    QUnit.test( "Substraction on Calculator Test", function( assert ) {
      button_8.click();
      button_sub.click();
      button_4.click();
      button_res.click();
      assert.equal( $('#print').val(), 4, "8 - 4 must be 4" );
      button_clear.click();
    });

    QUnit.test("Multiply on Calculator Test", function( assert ) {
        button_8.click();
        button_mul.click();
        button_4.click();
        button_res.click();
        assert.equal( $('#print').val(), 32, "8 * 4 must be 32" );
        button_clear.click();
    });

    QUnit.test("Division on Calculator Test", function( assert ) {
        button_8.click();
        button_div.click();
        button_4.click();
        button_res.click();
        assert.equal( $('#print').val(), 2, "8 / 4 must be 2" );
        button_clear.click();
    });
});