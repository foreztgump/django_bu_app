var Stopwatch = function(element, options, time_limit, voice) {

  var timer = createTimer(),
	audio_backflow_in = new Audio('{% static 'audio/backflow-in.mp3' %}');
	audio_backflow = new Audio('{% static 'audio/backflow.mp3' %}');
	audio_fire_in = new Audio('{% static 'audio/fire-in.mp3' %}');
	audio_fire = new Audio('{% static 'audio/fire.mp3' %}');
	audio_reflect_in = new Audio('{% static 'audio/fire-in.mp3' %}');
	audio_reflect = new Audio('{% static 'audio/fire.mp3' %}');
	audio_lightning_in = new Audio('{% static 'audio/lightning-in.mp3' %}');
	audio_lightning = new Audio('{% static 'audio/lightning.mp3' %}');
	audio_5 = new Audio('{% static 'audio/5.mp3' %}');
	audio_4 = new Audio('{% static 'audio/4.mp3' %}');
	audio_3 = new Audio('{% static 'audio/3.mp3' %}');
	audio_2 = new Audio('{% static 'audio/2.mp3' %}');
	audio_1 = new Audio('{% static 'audio/1.mp3' %}');
    offset,
    clock,
    interval;

  // default options
  options = options || {};
  options.delay = options.delay || 1;

  // append elements
  element.appendChild(timer);

  // initialize
  reset();

  // private functions
  function createTimer() {
    return document.createElement("span");
  }

  function createButton(action, handler) {
    var a = document.createElement("a");
    a.href = "#" + action;
    a.innerHTML = action;
    a.addEventListener("click", function(event) {
      handler();
      event.preventDefault();
    });
    return a;
  }

  function start() {
    if (!interval) {
      offset = Date.now();
      interval = setInterval(update, options.delay);
    }
  }

  function stop() {
    if (interval) {
      clearInterval(interval);
      interval = null;
    }
  }

  function reset() {
    clock = 0;
    render(0);
  }

  function update() {
    clock += delta();
    render();

  }

  function render() {
    timer.innerHTML = clock / 1000;
    if (clock > time_limit) {
    	clock = 0;
    }
  }

  function delta() {
    var now = Date.now(),
      d = now - offset;

    offset = now;
    return d;
  }
  
  function play_voice_mode(num) {
	if (num == 1) { //backflow
		if (clock == 24) {
			audio_backflow_in.play()
		}
		else if (clock == 25) {
			countdown_voice(5)
		}
		else if (clock == 26) {
			countdown_voice(4)
		}
		else if (clock == 27) {
			countdown_voice(3)
		}
		else if (clock == 28) {
			countdown_voice(2)
		}
		else if (clock == 29) {
			countdown_voice(1)
		}
		else if (clock == 30) {
			audio_backflow.play()
		}
	}
	else if (num == 2) { //fire
		if (clock == 24) {
			audio_fire_in.play()
		}
		else if (clock == 25) {
			countdown_voice(5)
		}
		else if (clock == 26) {
			countdown_voice(4)
		}
		else if (clock == 27) {
			countdown_voice(3)
		}
		else if (clock == 28) {
			countdown_voice(2)
		}
		else if (clock == 29) {
			countdown_voice(1)
		}
		else if (clock == 30) {
			audio_fire.play()
		}
	}
	else if (num == 3) { //reflect
		if (clock == 24) {
			audio_reflect_in.play()
		}
		else if (clock == 25) {
			countdown_voice(5)
		}
		else if (clock == 26) {
			countdown_voice(4)
		}
		else if (clock == 27) {
			countdown_voice(3)
		}
		else if (clock == 28) {
			countdown_voice(2)
		}
		else if (clock == 29) {
			countdown_voice(1)
		}
		else if (clock == 30) {
			audio_reflect.play()
		}
	}
	else if (num == 4) { //lightning
		if (clock == 24) {
			audio_lightning_in.play()
		}
		else if (clock == 25) {
			countdown_voice(5)
		}
		else if (clock == 26) {
			countdown_voice(4)
		}
		else if (clock == 27) {
			countdown_voice(3)
		}
		else if (clock == 28) {
			countdown_voice(2)
		}
		else if (clock == 29) {
			countdown_voice(1)
		}
		else if (clock == 30) {
			audio_lightning.play()
		}
	}
  }
  
  function countdown_voice(num) {
	if (num == 1) {
		audio_1.play()
	}
	else if (num == 2) {
		audio_2.play()
	}
	else if (num == 3) {
		audio_3.play()
	}
	else if (num == 4) {
		audio_4.play()
	}
	else if (num == 5) {
		audio_5.play()
	}
  }

  // public API
  this.time_limit = time_limit;
  this.start = start;
  this.stop = stop;
  this.reset = reset;
};