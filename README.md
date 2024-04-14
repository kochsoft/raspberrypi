# About

This is a script collection for the Raspberry Pi 4B I am using at home
for a music player, retro gaming device, even video streaming.

# Disclaimer

These scripts are declared public domain but come with as little
warranty as is legally allowed, disclaiming fitness for any
particular purpose.

# Scripts

## fan_control.py

Finding that once the fan of my Argon m.2 casing for the Raspy 4 fires up,
it will never fire down again, I read some of the scripts found in
`/etc/argon`, most notably `argononed.py` and its dependency `argonregister.py`.

This lead to the very simple (it may be boiled down to about 5-7 lines of actually
counting code -- depending on how you count) script

```
fan_control [val in {0,..,100}]
```

for setting the fan speed manually. My use-case is, when automatic powering down
of that noisy thing fails, and `sensors` gives me something around 38 degree Celsius,
I can say: `fan_control 0` to turn it off. Now. No warranties for consequences given by me to anyone!
Overheating your device may damage it. But I reckon you know that already. Still.