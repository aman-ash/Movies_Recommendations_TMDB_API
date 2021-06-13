function play1() {
    /* Audio link for notification */
    var mp3 =
      '<source src="static/audio/ruko.mp3" type="audio/mpeg">';
    document.getElementById("sound").innerHTML =
      '<audio autoplay="autoplay">' + mp3 + "</audio>";
  }