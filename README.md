# Promus

**Promus** is a lightweight, event-driven Python framework for Raspberry Pi DIY hardware projects.  
Control LEDs, buzzers, ultrasonic sensors, and manage GPIO events with clean, modular code.

---

## Features

- Simple control of LEDs, buzzers, and ultrasonic sensors
- Event system: subscribe to and handle hardware events (on/off, flash, object detected, etc.)
- Supports multiprocessing for async hardware tasks
- Easy to extend for your own hardware classes

---

## Installation

Clone this repository and ensure you have `RPi.GPIO` installed:

```bash
git clone https://github.com/yehiashouman/promus.git
cd promus
# Make sure RPi.GPIO is installed:
# pip install RPi.GPIO
```

# Quick Example
```python
import RPi.GPIO as GPIO
from promus.led.SingleColorLed import SingleColorLed
from promus.media.Buzzer import Buzzer
from promus.sensor.Ultrasonic_HCSR04 import Ultrasonic_HCSR04
from promus.core.events import Event

# Setup
GPIO.setmode(GPIO.BCM)
led = SingleColorLed(12, GPIO)
buzzer = Buzzer(16, GPIO)
ultrasonic = Ultrasonic_HCSR04(13, 6, GPIO)

# Event handlers
def on_led_flash(evt):
    print("LED flashed!")

def on_buzzer_complete(evt):
    print("Buzzer completed!")

led.addEventListener(Event.EVT_COMPLETE, on_led_flash)
buzzer.addEventListener(Event.EVT_COMPLETE, on_buzzer_complete)

# Control hardware
led.flash(3, 0.2)
buzzer.buzz(800, 0.5)
ultrasonic.trigger()
```

# Core Classes
- Base: Root class for IDs and helpers
- Event / EventDispatcher: Event system (add/dispatch listeners)
- SingleColorLed: Simple LED control (on, off, flash)
- Buzzer: Sound output with events for completion
- Ultrasonic_HCSR04: Distance sensing and detection events


# Main Events
| Event Name        | Description               |
| ----------------- | ------------------------- |
| `on`              | LED/Buzzer turned ON      |
| `off`             | LED/Buzzer turned OFF     |
| `flash`           | LED flashed               |
| `complete`        | Flash or buzz completed   |
| `object_detected` | Object detected by sensor |
| `update`          | State/value updated       |

# Requirements
- Python 2.7 or 3.x
- RPi.GPIO or compatible GPIO library

## License
This project is licensed under the GNU General Public License v3.0 (GPL‑3.0).  
See the full text of the license here: [GNU GPL v3](https://www.gnu.org/licenses/gpl-3.0.en.html)
